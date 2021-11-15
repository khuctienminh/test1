
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Taro
import logging
from django.urls import reverse_lazy
# from django.urls.base import reverse
# from re import template
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib import messages

logger = logging.getLogger(__name__)

from .forms import InquiryForm,InquiryForm1,InquiryForm2
# Create your views here.
class IndexView(generic.TemplateView):
  template_name = 'index.html'

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class InquiryView1(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm1
    success_url = reverse_lazy('diary:inquiry1')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class InquiryView2(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm2
    success_url = reverse_lazy('diary:inquiry2')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
