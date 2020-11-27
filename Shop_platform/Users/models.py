from django.db import models
from django.contrib.auth.models import User
import glob, os 
from PIL import Image

# Create your models here.

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default="nopicture.jpeg", upload_to="profilepicture")

	
	def __str__(self):

		return self.user.username

	def get_queryset(self):

		return self.user.objects.all() 

	def get_object(self):

		return self.user

	
	def save(self, **kwargs):

		super().save()

		size = 1080, 1080
		image = Image.open(self.image.path)
		image.thumbnail(size)
		image.save(self.image.path)
