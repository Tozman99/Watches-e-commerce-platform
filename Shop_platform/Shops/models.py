from django.db import models
from Users.models import Profile
from django.urls import reverse 
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
from PIL import Image
# Create your models here.

class Shop(models.Model):

	name = models.CharField(max_length=30)
	owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)

	def save(self, *args, **kwargs):

		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):

		return f"{self.name} created by {self.owner}"

category_product = (

			("1", "Sport"),
			("2", "Tech"),
			("3", "Health"),
			("4", "Entertainement")
			)

#filestorage = FileSystemStorage(location="/media/productsphotos")

class Product(models.Model):

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to="productsphotos", default="nopicture.jpeg")
	slug = models.SlugField(unique=True)
	date = models.DateField(auto_now_add=True)
	seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
	available = models.BooleanField()
	price = models.DecimalField(max_digits=7, decimal_places=2, default=10.00)
	description = models.TextField(max_length=200)
	category = models.CharField(max_length=10, choices=category_product, default="Sport")
	quantity = models.IntegerField(default=1)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="products")

	def __str__(self):

		return f"{self.pk} :{self.name}"

	def save(self, *args, **kwargs):

		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

		size = 1080, 1080
		image = Image.open(self.image.path)
		image.thumbnail(size)
		image.save(self.image.path)

	def get_absolute_url(self):

		return reverse("shops:detail-product", kwargs={"shop_slug": self.shop.slug, "slug": self.slug})