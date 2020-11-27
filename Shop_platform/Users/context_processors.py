from django.shortcuts import get_object_or_404
from .models import Profile


def get_profile(request):

    profile = None

    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)

        return {"profile":profile}

    return {}