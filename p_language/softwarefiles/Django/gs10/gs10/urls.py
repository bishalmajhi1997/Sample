from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.Studentlist.as_view()),
    path('crete/',views.StudentCreate.as_view()),
    path('retrive/<int:pk>/',views.StudentRetrive.as_view()),
    path('update/<int:pk>/',views.StudentUpdate.as_view()),
    path('destroy/<int:pk>/',views.StudentDestroy.as_view())



]
