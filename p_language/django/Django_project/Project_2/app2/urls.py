from django.urls import path
from app2 import views
urlpatterns = [
    path("user1/",views.User1,name="users"),
    path("forms/",views.FormNameView,name="forms99"),
    path("forms2/",views.FormNameView2,name="forms2"),
    path("form3/",views.Student_Form,name="form3"),
    path("index/",views.index,name="index"),
]
