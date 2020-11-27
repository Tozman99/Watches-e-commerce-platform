from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from .signals import order_creation
from .models import Notification
from ast import literal_eval
from Shops.models import Product
from Orders.models import Order
from django.shortcuts import get_object_or_404
from Users.models import Profile
from ast import literal_eval

# Create your views here.


def get_item_list(json_order):

	sellers_and_items = []

	for (key, value) in json_order.items():

		id = key[3:]
		product = Product.objects.get(pk=id)
		product_seller = product.seller
		item_description = {
								"name": product.name,
								"ID": product.pk,
								"seller": product.seller,
								"quantities": value,
								}

		sellers_and_items.append(item_description)

	return sellers_and_items

def seller_notification(list_items_description):

	for item in list_items_description:

		message = "Congrats {}! You've sold {}X {}".format(item["seller"], item["quantities"], item["name"]) # - item ID:{}
		seller_notification = Notification(user=item["seller"], message=message, type="sell")
		seller_notification.save()

@receiver(order_creation, sender=Order)
def user_notifications(sender=Order, **kwargs):

	user = kwargs["user"]
	order = kwargs["order"]

	message_customer = f"Congrats {user}, you've made an order" #, here is the id of your order:{order.pk}
	list_of_items = get_item_list(order.shoplist)
	Notification.objects.create(user=user, message=message_customer, type="order")
	print(list_of_items)
	seller_notification(list_of_items)
	print(message_customer)
	#print(notification_seller)

def notif_list_view(request):

	user_profile = get_object_or_404(Profile, user=request.user)
	notifications = Notification.objects.all().filter(user=user_profile)
	notif_list = []
	"""
		for notification in notifications:

			index = notification.message.index(":")
			order_pk = notification.message[index+1:]
			order = Order.objects.get(pk=order_pk)
			notif_list.append(order_list)
	"""
	return render(request, "notifications/notifications_list.html", {"notifications": notifications})

def deserialize_json(json_object):

	object = literal_eval(json_object)

	return object
