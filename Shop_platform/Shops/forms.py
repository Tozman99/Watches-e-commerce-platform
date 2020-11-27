from .models import Shop, Product
from django import forms

class Shop_Form(forms.ModelForm):

	class Meta:

		model = Shop
		fields = ["name"]

class Product_Form(forms.ModelForm):

	class Meta:

		model = Product
		fields = ["name", "image", "price", "description"]


class Update_Form(forms.Form):

	choices = ((quantity, quantity) for quantity in range(1, 99))
	quantity = forms.ChoiceField(choices=choices)