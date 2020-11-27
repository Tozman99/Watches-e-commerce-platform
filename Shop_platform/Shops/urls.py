from django.urls import path, include
from .views import (
						create_shop_view,
						detail_shop_view,
						list_shop_view,
						create_product_view,
						detail_product_view,
						update_product_view,
						delete_product_view,
						shop_list_view,
						products_list_View,
						)
from django.conf.urls.static import static
from Shop_platform import settings



app_name = "shops"

urlpatterns = [
		
		path("creation/", create_shop_view, name="creation-shop"),
		path("shop/<slug:shop_slug>/", detail_shop_view, name="detail-shop"),
		path("list/", list_shop_view, name="shop-list"),
		path("shop/products/creation", create_product_view, name="create-product"),
		path("shop/<slug:shop_slug>/products/<slug:slug>/", detail_product_view, name="detail-product"),
		path("shop/<slug:shop_slug>/products/<slug:slug>/update", update_product_view, name="update-product"),
		path("shop/<slug:shop_slug>/products/<slug:slug>/delete", delete_product_view, name="delete-product"),
		path("shoppingcart/", shop_list_view, name="shopping-cart"),
		path("products/NewTrends", products_list_View, name="products-list"),

]