from django.shortcuts import render

# Create your views here.


from Api.models import Product,Category

from Api.Serializers import ProductSerializers,CategorySerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from rest_framework import authentication,permissions

from rest_framework_simplejwt.authentication import JWTAuthentication



class ProductListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProductSerializers

    queryset=Product.objects.all()

class ProductRetriveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=ProductSerializers

    queryset=Product.objects.all()


class categoryListCreateView(ListAPIView,CreateAPIView):

    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=CategorySerializer

    queryset=Category.objects.all()

class CategoryRetriveUpdateDestroyApiView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):


    authentication_classes=[JWTAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=CategorySerializer

    queryset=Category.objects.all()





    









