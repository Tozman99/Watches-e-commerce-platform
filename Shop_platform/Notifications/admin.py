from django.contrib import admin
from .models import Notification

# Register your models here.

@admin.register(Notification)
class Notification_Admin(admin.ModelAdmin):

	fields = ["user", "message"]
