from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('slimes/', views.slimes_index, name='index'),
    path('slimes/<int:slime_id>/', views.slimes_detail, name="detail"),
    path('slimes/create/', views.SlimeCreate.as_view(), name='slimes_create'),
    path('slimes/<int:pk>/update/', views.SlimeUpdate.as_view(), name="slimes_update"),
    path('slimes/<int:pk>/delete/', views.SlimeDelete.as_view(), name="slimes_delete"),
]