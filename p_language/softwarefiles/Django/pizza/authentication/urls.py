from django.urls import path
from . import views
urlpatterns=[
      path('',views.HelloAuthView.as_view(),name="Hello_auth"),
      path('signup/',views.UserCreateView.as_view(),name="sign_up")
]
