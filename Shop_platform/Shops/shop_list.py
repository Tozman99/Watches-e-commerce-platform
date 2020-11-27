from .models import Product
from ast import literal_eval
from django.shortcuts import get_object_or_404
from django.core import serializers


class Shopping_Cart:

	def __init__(self, request):

		self.cookie_session = request.session 

		if "shopping_cart" not in self.cookie_session:

			self.cookie_session["shopping_cart"] = {}

	def convert_to_json(self, product):

		product_data = serializers.serialize("json", [product, ], fields=("name", "price", "slug", "quantity"))

		return product_data

	def add_product(self, product_id):

		product = Product.objects.get(id=product_id)
		product_data = self.convert_to_json(product)
		self.cookie_session["shopping_cart"][f"{product.name}"] = product_data
		self.cookie_session.save()

	def receive_product(self, id):

		product = Product.objects.get(id=id)

		return product

	def deserialize_json(self, json_object):

		object = literal_eval(json_object)

		return object

	def create_products_list(self):

		product_list = []

		for product in self.cookie_session["shopping_cart"].values():

			product = literal_eval(product)
			id = product[0]["pk"]
			product = self.receive_product(id)
			product_list.append(product)

		return product_list

	def get_quantity(self):
		
		quantities = []
		
		for product in self.cookie_session["shopping_cart"].values():

			product = literal_eval(product)
			quantity = product[0]["fields"]["quantity"]
			id = product[0]["pk"]
			object = Product.objects.get(pk=id)
			quantities.append((object.name, quantity))

		return quantities

	def get_total_price(self, quantity=1):

		products = self.create_products_list()
		price = 0

		for product in products:

			price += product.price * quantity

		return price

	def remove_product(self, product, products):

		shop_list_items = products
		print(shop_list_items)
		del self.cookie_session["shopping_cart"][str(product.name)]
		shop_list_items.remove(product)

	def total_price_shoplist(self, shoplist_dict):

		price = 0

		for (product_pk, quantity) in shoplist_dict.items():

			product = Product.objects.get(pk=int(product_pk))

			price += int(quantity) * product.price 

		return total_price

	def clear_shopping(self, products):

		self.cookie_session["shopping_cart"].clear()
		products.clear()
		self.cookie_session.save()







