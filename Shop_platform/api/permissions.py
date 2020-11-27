from rest_framework import permissions
from django.shortcuts import get_object_or_404
from Users.models import Profile


class isOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):

        if request.method == permissions.SAFE_METHODS:

            return True

        user_profile = get_object_or_404(Profile, user=request.user)
        print(user_profile, obj.seller)
        return user_profile == obj.seller