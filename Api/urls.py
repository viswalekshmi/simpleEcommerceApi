from django.urls import path

from Api import views

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns=[

    path("products/",views.ProductListCreateView.as_view()),

    path("products/<int:pk>/",views.ProductRetriveUpdateDestroyView.as_view()),

    path("category/",views.categoryListCreateView.as_view()),

    path("category/<int:pk>/",views.CategoryRetriveUpdateDestroyApiView.as_view()),

    path("token/",TokenObtainPairView.as_view()),

    path("token/refresh/",TokenRefreshView.as_view())


]