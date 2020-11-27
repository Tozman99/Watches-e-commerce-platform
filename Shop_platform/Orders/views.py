from django.shortcuts import get_object_or_404, render
from .models import Order
from Users.models import Profile
from Shops.models import Product

def order_list_view(request):

	user_profile = get_object_or_404(Profile, user=request.user)
	user_orders = Order.objects.all().filter(customer=user_profile)
	orders_dict = {}
	products_list = []

	for order in user_orders:

		order_products = order.shoplist

		for product_pk in order_products.keys():

			product_pk = product_pk[3:]
			product = Product.objects.get(id=product_pk)
			products_list.append(product)

		
		if f"ID-{order.pk}" not in orders_dict:

			price = price_calc(products_list)
		
			orders_dict[f"ID-{order.pk}"] = {"id": order.pk , "products":products_list, "price": price}
			products_list = []

	return render(request, "orders/order_list.html", {"orders": orders_dict})

def order_to_deliver_view(request):



	return render(request, "orders/order_deliver.html", {})

def price_calc(products_list):

	price = 0

	for product in products_list:

		price += product.price

	return price