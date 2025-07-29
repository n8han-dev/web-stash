
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello/details/<int:id>', views.details, name='details'),
    path('hello/testing', views.testing, name='tmp')
]