"""Shop_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .settings import MEDIA_URL, MEDIA_ROOT 
from django.conf.urls.static import static
from .settings import STATIC_URL, STATIC_ROOT
from shop_platform_app.views import test_view
#from shop_platform_app.views import home_view


#path("home/", home_view, name="home_view"),
#path("shops/", include("shops.urls")),
#path("orders/", include("orders.urls")),
#path("notifications/", include("notifications.urls")),


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Users.urls")),
    path("shops/", include("Shops.urls")),
    path("orders/", include("Orders.urls")),
    path("notifications/", include("Notifications.urls")),
    path("api/", include("api.urls", namespace="web-api")),
	path("password_reset/", auth_views.PasswordResetView.as_view(), name="password-reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path("test", test_view, name="test"),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

#urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)