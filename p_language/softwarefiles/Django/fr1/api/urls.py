from django.urls import path
from api import views
urlpatterns=[
     path("",views.ExpenseListAPIView.as_view(),name="expenses"),
     path("<int:id>/",views.ExpenseDetailAPIView.as_view(),name="expensedetails")
]
