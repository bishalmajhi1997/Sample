from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="shophome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("Productview/",views.productView,name="Productview"),
    path("checkout/",views.checkout,name="checkout"),


]