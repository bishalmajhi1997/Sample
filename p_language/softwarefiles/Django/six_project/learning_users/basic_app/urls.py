from django.urls import path
from basic_app import views
#Template url
urlpatterns=[
          path("register/",views.register,name="register"),
          path('user_login',views.user_login,name='user_login'),
]
