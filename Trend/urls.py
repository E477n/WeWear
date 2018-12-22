from django.urls import path
from . import views

app_name = 'Trend'
urlpatterns = [
    # /Trend/
    path('trend/', views.trend, name='trend'),
    path('trend/loadMore/', views.loadMore, name="loadMore"),
    path('trend/likeCount/', views.likeCount, name="likeCount")
]