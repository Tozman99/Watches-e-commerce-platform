from django.forms import ModelForm 
from .models import Address
from django_countries.fields import CountryField

class Address_Form(ModelForm):

	country = CountryField().formfield()

	class Meta:

		model = Address
		fields = ["country", "city", "street", "postal_code"]