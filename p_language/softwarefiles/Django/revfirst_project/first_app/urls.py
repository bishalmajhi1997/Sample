from django.urls import path
from first_app import views

urlpatterns=[
        path("help/",views.help,name="help"),
        path("raja/",views.raja,name="raja")
]
