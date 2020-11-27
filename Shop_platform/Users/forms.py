from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile

class User_Form(UserCreationForm):

	class Meta:

		model = User 
		fields = ["username", "password1", "password2", "email",
					"first_name", "last_name"]


class Profile_Form(ModelForm):


	class Meta:

		model = Profile
		exclude = ["user"]
