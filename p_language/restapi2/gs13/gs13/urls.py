"""gs13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.StudentListAPIView.as_view(),name="student"),
    path('create/',views.StudentCreateAPIView.as_view(),name="studentc"),
    path('retrieve/<int:pk>/',views.StudentRetrieveAPIView.as_view(),name="studentcv"),
    path('update/<int:pk>/',views.StudentUpdateAPIView.as_view(),name="studentcvu"),
    path('delete/<int:pk>/',views.StudentDeleteAPIView.as_view(),name="studentpkd"),
]
