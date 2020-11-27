from Users.models import Profile
from Shops.models import Shop, Product
from rest_framework.serializers import HyperlinkedModelSerializer , ModelSerializer, StringRelatedField, HyperlinkedIdentityField
from rest_framework import serializers



class ProfileSerializer(HyperlinkedModelSerializer):
    
    user = StringRelatedField(source="user.username")
    url = HyperlinkedIdentityField(view_name="web-api:profile-detail")

    class Meta:

        model = Profile
        fields = ["url", "id", "user", "image"]


class ShopSerializer(ModelSerializer):

    owner = StringRelatedField(source="owner.user.username")
    url = HyperlinkedIdentityField(view_name="web-api:shop-detail", lookup_field="slug")
    #products = StringRelatedField(many=True)
    products = HyperlinkedIdentityField(view_name="web-api:product-detail",many=True, lookup_field="slug")
   
    class Meta:

        model = Shop
        fields = ["url", "id", "name", "owner", "products"]

class ProductSerializer(ModelSerializer):

    url = HyperlinkedIdentityField(view_name="web-api:product-detail", lookup_field="slug")
    shop = StringRelatedField(source="shop.name")
    seller = StringRelatedField(source="seller.user.username")

    class Meta:

        model = Product
        fields = ["url", "id", "name", "image", "date", "seller", "available", "price", "description", "category", "quantity", "shop"]
