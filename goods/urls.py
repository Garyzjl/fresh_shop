"""__author__ - Gary"""
from django.urls import path
from goods import views


urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    # 详情
    path('detail/<int:id>/', views.detail, name='detail'),
    # 商品列表
    path('fruit_list/', views.fruit_list, name='fruit_list'),
]
