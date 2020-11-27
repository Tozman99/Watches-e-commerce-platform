from django.urls import path
from .views import order_list_view, order_to_deliver_view

app_name = "orders"


urlpatterns = [
	path("yourorder/", order_list_view, name="order_list"),
	#path("orderToDeliver/", order_to_deliver_view, name="order-to-deliver")
]