from django.urls import path
from .views import ( ProfileListView, ProfileDetailView, 
                        ShopListView, ShopDetailView, 
                            ProductDetailView )
from Users.models import Profile
from Shops.models import Shop, Product

app_name = "api"

urlpatterns = [

    path("profiles/", ProfileListView.as_view(queryset=Profile.objects.all()), name="profile-list"),
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile-detail"),
    path("shops/", ShopListView.as_view(queryset=Shop.objects.all()), name="shop-list"),
    path("shops/<slug:slug>/", ShopDetailView.as_view(), name="shop-detail"),
    path("products/<slug:slug>/", ProductDetailView.as_view(lookup_field="slug"), name="product-detail"),
    #path("products/", ProductListView.as_view(), name="product-list")

]