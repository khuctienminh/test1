
import re
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Taro
import logging
from django.urls import reverse_lazy
from django.urls.base import reverse
# from . import template
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib import messages
from accounts.models import CustomUser
from .models import Tag,Taro
from django.http import HttpResponseRedirect
logger = logging.getLogger(__name__)

from .forms import InquiryForm,InquiryForm1,InquiryForm2,UserInfoCreateForm,TaroCreateForm
# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('taro:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class InquiryView1(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm1
    success_url = reverse_lazy('taro:inquiry1')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class InquiryView2(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm2
    success_url = reverse_lazy('taro:inquiry2')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class UserInfoCreateView(LoginRequiredMixin,generic.UpdateView):
    model = CustomUser
    template_name = "usercreate.html"
    form_class = UserInfoCreateForm
    success_url = reverse_lazy('taro:userinfocreate')

    def get_success_url(self):
        return reverse_lazy('taro:userinfo',
        kwargs={'pk':self.kwargs['pk']})
    def form_valid(self,form):
        messages.success(self.request,'情報を更新しました。')
        return super().form_valid(form)

    def form_valid(self,form):
        messages.error(self.request,'情報の更新に失敗しました。')
        return super().form_valid(form)

class UserInfoView(LoginRequiredMixin,generic.DetailView):
    model = CustomUser
    template_name = "userinfomation.html"

class TopView(generic.TemplateView):
  template_name = 'top.html'


class TaroListView(LoginRequiredMixin,generic.ListView):
    model = Taro
    template_name= 'taro_list.html'

    def get_queryset(self):
        portfolio = Taro.objects.filter(user=self.request.user).order_by('-created_at')
        return portfolio



class TaroCreateView(LoginRequiredMixin,generic.CreateView):
    model = Taro
    template_name = "taro_create.html"
    form_class = TaroCreateForm
    success_url = reverse_lazy('taro:taro_list')

    def form_valid(self,form):
        taro = form.save(commit=False)
        taro.user = self.request.user
        taro.save()
        messages.success(self.request,'taroを作成しました。')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'taroの作成に失敗しました。')
        return super().form_invalid(form)


class TaroDetailView(LoginRequiredMixin,generic.DetailView):
    model = Taro
    template_name = "taro_detail.html"

    def get_context_data(self, **kwargs):
        stuff = get_object_or_404(Taro, id=self.kwargs['pk'])
        data = super().get_context_data(**kwargs)
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        data['total_likes'] = total_likes
        data['liked'] = liked
        return data



class TaroUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Taro
    template_name = "taro_update.html"
    form_class = TaroCreateForm
    
    def get_success_url(self):
        return reverse_lazy('taro:taro_detail',
        kwargs={'pk':self.kwargs['pk']})
    def form_valid(self,form):
        messages.success(self.request,'taroを更新しました。')
        return super().form_valid(form)

    def form_valid(self,form):
        messages.error(self.request,'taroの更新に失敗しました。')
        return super().form_valid(form)
class TaroDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Taro
    template_name = "taro_delete.html"
    success_url = reverse_lazy('taro:taro_list')

    def delete(self,request,*args,**kwargs):
        messages.success(self.request,'taroを削除しました。')
        return super().delete(request,*args,**kwargs)


class KensakuTaroListView(generic.ListView):
    model = Taro
    template_name= 'kensakutaro_list.html'

    def get_queryset(request):
        portfolio = Taro.objects.all()
        return portfolio

def LikeView(request, pk):
    taro = get_object_or_404(Taro, id=request.POST.get('taro_id'))
    liked = False
    if taro.likes.filter(id=request.user.id).exists():
        taro.likes.remove(request.user)
        liked = False
    else:
        taro.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('taro:taro_detail', args=[str(pk)]))
    