from django.urls import path
from app1 import views
urlpatterns = [
    path("",views.index,name="index"),
    path('home/',views.Home,name="home"),
    path('contact/',views.cotact,name="contact"),
    path("webpage/",views.Webpage,name="webpage"),
    path("webpage1/",views.webpage1,name="webpage")
]
