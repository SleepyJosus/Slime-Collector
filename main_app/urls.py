from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('slimes/', views.slimes_index, name='index'),
    path('slimes/<int:slime_id>/', views.slimes_detail, name='detail'),
    path('slimes/create/', views.SlimeCreate.as_view(), name='slimes_create'),
    path('slimes/<int:pk>/update/', views.SlimeUpdate.as_view(), name='slimes_update'),
    path('slimes/<int:pk>/delete/', views.SlimeDelete.as_view(), name='slimes_delete'),
    path('slimes/<int:slime_id>/assoc/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyListView.as_view(), name='toy_list'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/', views.ToyDetailView.as_view(), name='toy_detail'),
    path('toys/<int:pk>/update/', views.ToyUpdateView.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete/', views.ToyDeleteView.as_view(), name='toy_delete'),
]