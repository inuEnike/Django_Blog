from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
      path('', views.home, name='home'),
      path('author/<str:username>/', views.author, name='author'),
      path('comment/<int:pk>/', views.comment, name='comment'),
      # path('all_comments/<int:pk>/', views.AllComments, name='all_comments'),
      path('logout/', views.logout, name='logout'),
      path('post/<pk>/', views.post, name='post')
]