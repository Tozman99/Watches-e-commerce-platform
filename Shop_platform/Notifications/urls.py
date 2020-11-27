from django.urls import path
from .views import notif_list_view

app_name = "notifications"

urlpatterns = [
		
		path("list/", notif_list_view, name="notif_list")

]