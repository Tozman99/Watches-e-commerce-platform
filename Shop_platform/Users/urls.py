from django.urls import path, include
from .views import home_view
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import User_Registration_View, profile_View, profile_other_user, story_view, services_view, tutorials_view
from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
	
	path("home/", home_view, name="home"),
	path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
	path("registration/", User_Registration_View, name="registration"),
	path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
	path("accounts/profile/", profile_View, name="profile"),
	path("change-password/", auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("users:password_change_done")), name="Change_password"),
	path("change-password/done", auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
	#path("accounts/<int:id>/", profile_other_user, name="Other_User_View"),
	path("story/", story_view, name="story"),
	path("services/", services_view, name="services"),
	path("tutorials/", tutorials_view, name="tutorials"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
