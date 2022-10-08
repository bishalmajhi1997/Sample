from django.urls import path
from testapp import views
urlpatterns=[
       path("",views.index,name="index"),
       path("signup/",views.register,name='register'),
       path("activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})",views.activate,name="activate"),
       path("user_login/",views.user_login,name="user_login"),
       path("uer_logout/",views.user_logout,name="user_logout"),
]
