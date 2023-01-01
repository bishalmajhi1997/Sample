from django.urls import path
from app3 import views
urlpatterns = [
    path("",views.index,name="index"),
    path("registrations/",views.register,name="register"),
    path("login/",views.user_login,name="login"),
    
]
