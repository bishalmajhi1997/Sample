from django.urls import path
from proTwo import views
urlpatterns=[
          path("",views.users,name="users"),
]
