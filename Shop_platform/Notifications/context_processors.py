from .models import Notification
from django.contrib.auth.models import User
from Users.models import Profile
from django.shortcuts import get_object_or_404


def get_notifications(request):

    if request.user.is_authenticated:
        notification_list = []
        profile = get_object_or_404(Profile, user=request.user)
        notifications = Notification.objects.all().filter(user=profile)

        for notification in notifications:
            
            notification_list.append(notification.message)

        return {'notifications':notification_list}
    return {}
    