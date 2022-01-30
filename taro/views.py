
from itertools import count
from pickle import TRUE
import re
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Taro
import logging
from django.db import models
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.urls.base import reverse
# from . import template
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib import messages
from accounts.models import CustomUser
from .models import Tag,Taro
from django.http import HttpResponseRedirect
from django.db.models import Q
logger = logging.getLogger(__name__)
from django.db.models import Count

from .forms import InquiryForm,InquiryForm1,InquiryForm2,UserInfoCreateForm,TaroCreateForm
from django.utils import timezone
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

    

    def get_context_data(self,**kwargs):
        man = self.request.user
        data = super().get_context_data(**kwargs)

        timecreate = man.date_joined
        timenow = timezone.now()
        a = timenow - timecreate
        b = a.days
        post = Taro.objects.filter(user=man).order_by('-created_at')
        totalpost = post.count()
        postlike = man.likes.all()

        erabu = self.request.GET.get('newsletter_sub')
        if erabu == 'お気に入り投稿':
            erabu = True
        else:
            erabu = False

        data['erabu'] = erabu
        data['time'] = b
        data['totalpost'] = totalpost
        data['postlike'] = postlike
        return data

    




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


class TaroDetailView(generic.DetailView):
    model = Taro
    template_name = "taro_detail.html"

    def get_context_data(self, **kwargs):
        stuff = get_object_or_404(Taro, id=self.kwargs['pk'])
        data = super().get_context_data(**kwargs)

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

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




def LikeView(request, pk):
    taro = get_object_or_404(Taro, id=request.POST.get('taro_id'))
    liked = False
    if taro.likes.filter(id=request.user.id).exists():
        taro.likes.remove(request.user)
        liked = False
    else:
        taro.likes.add(request.user)
        liked = True


    man = get_object_or_404(CustomUser,username=taro.user)
    post = Taro.objects.filter(user=man)
    usertotallikes = 0
    for p in post:
        a = p.likes.count()
        usertotallikes = usertotallikes + a
    man.likerecieve = usertotallikes
    man.save()
 
    taro.likestotal = taro.likes.count()
    taro.save()


    return HttpResponseRedirect(reverse('taro:taro_detail', args=[str(pk)]))


class MyPageView(generic.DetailView):
    model = CustomUser
    template_name = "mypage.html"

    def get_context_data(self,**kwargs):
        man = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        data = super().get_context_data(**kwargs)

        erabi = self.request.GET.get('toujun')
        if erabi == 'お気に入り順位':
            erabi = True
        else:
            erabi = False
        timecreate = man.date_joined
        timenow = timezone.now()
        a = timenow - timecreate
        b = a.days
        if erabi == False:
            post = Taro.objects.filter(user=man).order_by('-created_at')
        else:
            post = Taro.objects.filter(user=man).order_by('-likestotal')
        
        totalpost = post.count()
        
        data['time'] = b
        data['totalpost'] = totalpost
        data['post'] = post
        data['erabi'] = erabi
        return data


class KensakuView(generic.TemplateView):
    template_name= 'kensaku.html'
    success_url = reverse_lazy('taro:kensaku-kekka')


    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        portfolio = Taro.objects.order_by('-likestotal')[:3] 
        man = CustomUser.objects.order_by('-likerecieve')[:3]
        data['portfolio'] = portfolio
        data['man'] = man
        return data

    

class KensakuKekkaView(generic.ListView):
    model = Taro
    template_name= 'kensaku_kekka.html'


    
    def get_context_data(self,**kwargs):
        data = super().get_context_data(**kwargs)
        kensakunaiyo = self.request.GET.get('kensakunaiyo')
        kenmei = self.request.GET.get('kenmei')
        age = self.request.GET.get('age')
        okane = self.request.GET.get('okane')

        userkensa = self.request.GET.get('userkensa')


        if okane:
            if okane == "1":
                okane1 = (0,1000)
            elif okane == "2":
                okane1 = (1000,10000)
            elif okane == "3":
                okane1 = (10000,50000)
            elif okane == "4":
                okane1 = (50000,100000)
            elif okane == "5":
                okane1 = (100000,1000000)
                
        
        if okane:
            if kensakunaiyo:
                if kenmei:
                    if age:
                        portfolio = Taro.objects.filter(okane__range=(okane1)).filter(kenmei=kenmei).filter(user__age=age).filter(
                            Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo)| Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                        )
                    else:
                        portfolio = Taro.objects.filter(okane__range=(okane1)).filter(kenmei=kenmei).filter(
                            Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                        )
                elif age:
                    portfolio = Taro.objects.filter(okane__range=(okane1)).filter(user__age=age).filter(
                        Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                    )
                else:
                    portfolio = Taro.objects.filter(okane__range=(okane1)).filter(
                        Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(tag__tagname__icontains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                    )
            else:
                if kenmei:
                    if age:
                        portfolio = Taro.objects.filter(okane__range=(okane1)).filter(kenmei=kenmei).filter(user__age=age)
                    else:
                        portfolio = Taro.objects.filter(okane__range=(okane1)).filter(kenmei=kenmei)
                elif age:
                    portfolio = Taro.objects.filter(okane__range=(okane1)).filter(user__age=age)
                else:
                    portfolio = Taro.objects.filter(okane__range=(okane1))
        else:
            if kensakunaiyo:
                if kenmei:
                    if age: 
                        portfolio = Taro.objects.filter(kenmei=kenmei).filter(user__age=age).filter(
                            Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(okane__icontains=kensakunaiyo) | Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                        )
                    else:
                        portfolio = Taro.objects.filter(kenmei=kenmei).filter(
                            Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(okane__icontains=kensakunaiyo) | Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                        )
                elif age:
                    portfolio = Taro.objects.filter(user__age=age).filter(
                        Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(okane__icontains=kensakunaiyo) | Q(tag__tagname__contains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                    )
                else:
                    portfolio = Taro.objects.filter(
                        Q(areaname__icontains=kensakunaiyo) | Q(eki__icontains=kensakunaiyo) | Q(okane__icontains=kensakunaiyo) | Q(tag__tagname__icontains=kensakunaiyo) | Q(naiyou__icontains=kensakunaiyo)
                    )
            else:
                if kenmei:
                    if age:
                        portfolio = Taro.objects.filter(kenmei=kenmei).filter(user__age=age)
                    else:
                        portfolio = Taro.objects.filter(kenmei=kenmei)
                elif age:
                    portfolio = Taro.objects.filter(user__age=age)
                else:
                    portfolio = Taro.objects.all()

        theogio = portfolio.order_by('-created_at')
        port = portfolio.order_by('-likestotal')

        if userkensa:
            userkensaku = CustomUser.objects.filter(Q(username__icontains=userkensa))
            data['userkensaku'] = userkensaku
            if userkensaku != TRUE:
                userkensakunothing = 'nothing'
                data['userkensakunothing'] = userkensakunothing
            
        
        data['theogio'] = theogio
        data['portfolio'] = port

        return data


    
