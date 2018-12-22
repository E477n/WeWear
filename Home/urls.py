from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    # /Home/
    path('', views.index, name='index'),
    path('logIn/', views.logIn, name='logIn'),
    path('signIn/', views.signIn, name='signIn'),
    path('getUserInfo/', views.getUserInfo, name='getUserInfo'),
    path('insertStyle1/', views.insertStyleInfo1, name='insertStyleInfo1'),
    path('insertStyle2/', views.insertStyleInfo2, name='insertStyleInfo2'),
    path('startMatching/', views.startMatching, name='startMatching'),
    # /Home/1/
    # path('Home/<int:User_id>/', views.detail, name='detail'),
]