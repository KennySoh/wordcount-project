from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eggs/', views.egg),
    path('count/', views.count, name='count'),
    path('aboutus/', views.about, name='about')
]
