from django.contrib import admin
from .models import Shop, Product

# Register your models here.

@admin.register(Shop)
class Shop_Admin(admin.ModelAdmin):

	fields = ("name", "owner", "slug")
	prepopulated_fields = {"slug": ("name", )}
	list_display = ("name", )


@admin.register(Product)
class Product_Admin(admin.ModelAdmin):

	fields = ("name", "image", "slug", "seller", "available",
				 "price", "shop", "description")

	prepopulated_fields = {"slug": ("name", )}
	list_display = ("name", "price", "available")