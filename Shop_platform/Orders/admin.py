from django.contrib import admin
from .models import Address, Order

# Register your models here.

@admin.register(Address)
class Address_Admin(admin.ModelAdmin):

	fields = ["country", "city", "street", "postal_code"]
	list_display = ("country", )


@admin.register(Order)
class Order_Admin(admin.ModelAdmin):

	fields = ["address", "customer", "paid", "shoplist"]