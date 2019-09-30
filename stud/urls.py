from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns=[
    path('', views.index,name="index"),
    path('login/', views.login,name="login"),
]