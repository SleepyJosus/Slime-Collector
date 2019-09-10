from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('slimes/', views.slimes_index, name='index'),
    path('slimes/<int:slime_id>/', views.slimes_detail, name="detail")
]