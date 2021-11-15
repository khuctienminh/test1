from django.urls import path

from . import views

app_name = 'taro'

urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('inquiry/form',views.InquiryView.as_view(),name = 'inquiry'),
    path('inquiry/form1',views.InquiryView1.as_view(),name = 'inquiry1'),
    path('inquiry/form2',views.InquiryView2.as_view(),name = 'inquiry2'),
]