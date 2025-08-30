
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('404', views.page404, name='404'),
    path('article/<slug:slug>/', views.article_detail, name="article_detail"),
]