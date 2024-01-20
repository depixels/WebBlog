from django.urls import path
from . import views

app_name = 'blog'  # 应用命名空间

urlpatterns = [
    path('post/new/', views.post_new, name='post_new'), # ..
    path('posts/', views.post_list, name='post_list'), # ..
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.chapter_list, name='chapter_list'),
    path('chapters/<int:pk>/', views.chapter_detail, name='chapter_detail'), #..
    path('chapters/<int:pk>/articles/', views.chapter_articles, name='chapter_articles'), #..
]
