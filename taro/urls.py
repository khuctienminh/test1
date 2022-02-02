from django.urls import path
from . import views

app_name = 'taro'

urlpatterns = [
    
    path('',views.IndexView.as_view(),name = 'index'),
    path('top',views.TopView.as_view(),name = 'top'),
    path('inquiry/form',views.InquiryView.as_view(),name = 'inquiry'),
    path('inquiry/form1',views.InquiryView1.as_view(),name = 'inquiry1'),
    path('inquiry/form2',views.InquiryView2.as_view(),name = 'inquiry2'),
    path('userinfocreate/<int:pk>/',views.UserInfoCreateView.as_view(),name = 'userinfocreate'),
    path('userinfo/<int:pk>/',views.UserInfoView.as_view(),name = 'userinfo'),
    path('taro-list/',views.TaroListView.as_view(),name="taro_list"),
    path('kensaku-kekka/',views.KensakuKekkaView.as_view(),name="kensaku-kekka"),
    path('kensaku/',views.KensakuView.as_view(),name="kensaku"),
    path('taro-create/',views.TaroCreateView.as_view(),name="taro_create"),
    path('taro-detail/<int:pk>/',views.TaroDetailView.as_view(),name="taro_detail"),
    path('taro-update/<int:pk>/',views.TaroUpdateView.as_view(),name="taro_update"),
    path('taro-delete/<int:pk>/',views.TaroDeleteView.as_view(),name="taro_delete"),
    path('like/<int:pk>/',views.LikeView,name='like_taro'),
    path('mypage/<int:pk>/',views.MyPageView.as_view(),name = 'mypage'),

]