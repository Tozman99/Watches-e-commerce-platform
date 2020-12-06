from .shop_list import Shopping_Cart 
from ast import literal_eval
from .models import Product, Shop
from django.shortcuts import get_object_or_404
from Users.models import Profile

def get_shoplist(request):

    #shoppingcart = request.session["shoppingcart"]
    cookie_session = request.session

    if "shopping_cart" in cookie_session:

        shop_cart_products = []
        index = 0

        for product_name, product_obj_json in cookie_session["shopping_cart"].items():
            product_obj = literal_eval(product_obj_json)
            #print(product_name, product_obj[0]["pk"])
            product = Product.objects.get(pk=product_obj[0]["pk"])
            shop_cart_products.append(product)
        print(shop_cart_products)
        return {"shoppingcart_products": shop_cart_products}

    return {}

def get_shop(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

        if Shop.objects.filter(owner=profile).exists():
            shop = get_object_or_404(Shop, owner=profile)

            return {"shop": shop}
        else:    
            return {}

    return {}

