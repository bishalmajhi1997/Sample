from django.urls import path
from product import views

urlpatterns = [
    # path("",views.api_home,name="apihome"),
    path("fcreate/",views.product_alt_view,name="ndnd "),
    path("fcreate/<int:pk>/",views.product_alt_view,name=""),
    path("create/list/",views.ProductCreateAPIView.as_view()),
    path("create/",views.ProductListCreateAPIView.as_view()),
    path("<int:pk>/",views.ProductDetailAPIView.as_view()),
    path("<int:pk>/update/",views.ProductUpdateAPIView.as_view()),
    path("<int:pk>/delete/",views.ProductDestroyAPIView.as_view()),
    path("mixin/",views.ProductMixinView.as_view()),
    path("mixin/<int:pk>/",views.ProductMixinView.as_view())
]
