from django.db import models
from django_countries.fields import CountryField
from Users.models import Profile
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Address(models.Model):
	
	country = CountryField(blank_label="Choose your country")
	city = models.CharField(max_length=30)
	street = models.CharField(max_length=100)
	postal_code = models.IntegerField()

	def __str__(self):

		return f"En {self.country.name}, ville: {self.city}, rue: {self.street} {self.postal_code}"


class Order(models.Model):

	customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
	paid = models.BooleanField(default=False)
	date = models.DateField(auto_now=True)
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	shoplist = JSONField(blank=True, default=dict)

	def __str__(self):

		return f"client : {self.customer} - commande numero: {self.id}"

	class Meta:

		ordering = ['-date']



