from django.shortcuts import render
from .serializers import ProfileSerializer, ShopSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Users.models import Profile
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.shortcuts import get_object_or_404
from Shops.models import Shop, Product
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
from .permissions import isOwnerOrReadOnly


# Create your views here.
"""
@api_view(["GET"])
def ProfileListView(request):

    if request.method == "GET":

        queryset = Profile.objects.all()
        serializer = ProfileSerializer(queryset, many=True)

        return Response(serializer.data, status=200)

    return None

"""

class ProfileListView(ListAPIView):
    
    throttle_classes = [UserRateThrottle]

    def get(self, request):

        serializer = ProfileSerializer(self.get_queryset(), many=True, context={"request":request})
        data = serializer.data

        return Response(data, status=200)


class ProfileDetailView(RetrieveAPIView):

    throttle_classes = [UserRateThrottle]

    def get(self, request, pk):
        
        serializer = None
        if request.method == "GET":
            profile = get_object_or_404(Profile, pk=pk)
            serializer = ProfileSerializer(profile, context={"request":request})

        return Response(serializer.data, status=200)

class ShopListView(ListAPIView):
    
    throttle_classes = [UserRateThrottle]

    def get(self, request):

        serializer = ShopSerializer(self.get_queryset(), many=True, context={"request":request})
        data = serializer.data

        return Response(data, status=200)

class ShopDetailView(RetrieveAPIView):
    
    throttle_classes = [UserRateThrottle]

    def get(self, request, slug):
        
        serializer = None
        if request.method == "GET":
            shop = get_object_or_404(Shop, slug=slug)
            serializer = ShopSerializer(shop, context={"request":request})

        return Response(serializer.data, status=200)


class ProductDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer
    permission_classes = [isOwnerOrReadOnly, permissions.IsAdminUser]
    throttle_classes = [UserRateThrottle]

    
    def get(self, request, slug):
        
        serializer = None
        if request.method == "GET":
            product = get_object_or_404(Product, slug=slug)
            serializer = ProductSerializer(product, context={"request":request})

        return Response(serializer.data, status=200)

    def get_queryset(self):

        queryset = Product.objects.all()

        return queryset

 
