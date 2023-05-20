from django.urls import path
from drawing import views

urlpatterns = [
    path('', views.home, name='home'),
]
