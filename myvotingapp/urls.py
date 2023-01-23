from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'homes'),
    path('like/', views.like, name='like'),
    path('dislike/', views.dislike, name='dislike'),
]
