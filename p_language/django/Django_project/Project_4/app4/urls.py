
from django.urls import path
from app4 import views
urlpatterns = [
    path('resgister/',views.regsitrations,name="registraions"),
    path('index/',views.index,name="index"),
    path('user_login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
]
