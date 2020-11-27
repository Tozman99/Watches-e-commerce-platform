from django.shortcuts import render,redirect, get_object_or_404
from .forms import User_Form, Profile_Form
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail, send_mail
from Shop_platform.settings import EMAIL_HOST_USER
from .models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PIL import Image
from Shops.models import Shop, Product


def home_view(request):
	
	products = Product.objects.all()[0:4]
	profile = None
	if request.user.is_authenticated:
		profile = get_object_or_404(Profile, user=request.user)
	
	return render(request, "users/home.html", {"products":products, "profile":profile})

def resize_image(self, picture):

		image = picture.resize((1080, 1080))

		return image 


def User_Registration_View(request):

	form = User_Form()

	if request.method == "POST":
		form = User_Form(request.POST)

		if form.is_valid():

			form.save()
			obj = get_object_or_404(User, username=request.POST["username"])
			Profile.objects.create(user=obj)

			user_mail = request.POST["email"]
			message = ("Hello there", "This is an automated message", EMAIL_HOST_USER, [user_mail])
			print("POST",EMAIL_HOST_USER, user_mail)
			send_mail("Hello there", "Hello, This is Your username: {} and your password {}".format(request.POST["username"], request.POST["password1"]), EMAIL_HOST_USER, ["karim.sadiki@gmail.com"])

			#return redirect("login")
			return HttpResponseRedirect("../login")
		
		return render(request, "users/signup.html", {"form":form})

	return render(request, "users/signup.html", {"form":form})
 
	
	#else:
	#	return render(request, "registration/signup.html", {"form":form})
		

def profile_View(request):

	form = Profile_Form()
	obj = get_object_or_404(Profile, user=request.user.id)
	if request.method == "POST":
		
		form = Profile_Form(request.POST, request.FILES, instance=obj)
		if form.is_valid():
			print(request.FILES)
			obj.image = request.FILES["image"]
			form.save()		

			

	return render(request, "users/profile.html", {"person":obj, "form":form})

@login_required(login_url="/login/")
def profile_logout_view(request):

	return render(request, "users/logout.html", {})

def profile_other_user(request, id):

	user = get_object_or_404(Profile, pk=id)
	return render(request, "users/profile_other_user.html", {"user":user})


def story_view(request):

	return render(request, "users/ourstory.html", {})


def services_view(request):

	return render(request, "users/services.html", {})

def tutorials_view(request):
	
	profile = None
	shop = None
	
	if request.user.is_authenticated:

		profile = get_object_or_404(Profile, user=request.user)

		shop = Shop.objects.get(owner=profile)

	return render(request, "users/tutorials.html", {"profile": profile, "shop":shop})