from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.LCSStudent.as_view()),
    path('destroy/<int:pk>/',views.StudentRetrive.as_view())



]
