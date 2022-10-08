from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.StudentList.as_view()),
    path('create/',views.StudentCreate.as_view()),
    path('retrive/<int:pk>/',views.StudentRetrieve.as_view()),
    path('update/<int:pk>/',views.StudentUpdate.as_view()),
    path('delete/<int:pk>/',views.StudentDestroy.as_view()),
    path('listcreate/',views.StudentListCreate.as_view()),
    path('retrieveupdate/<int:pk>/',views.StudentRetrieveUpdate.as_view()),
    path('retrieveupdatedestroy/<int:pk>/',views.StudentRetrieveUpdateDestroy.as_view()),

    #path('destroy/<int:pk>/',views.StudentRetrive.as_view())



]
