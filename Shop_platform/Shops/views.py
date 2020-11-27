from django.shortcuts import render
from .models import Shop, Product
from .forms import Shop_Form, Product_Form, Update_Form
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from Users.models import Profile
from .shop_list import Shopping_Cart
from ast import literal_eval
from django.core.files.storage import FileSystemStorage
from Orders.models import Address, Order
from Notifications.signals import order_creation



# Create your views here.


def create_shop_view(request):
	
	form = Shop_Form()
	owner = get_object_or_404(Profile, user=request.user)

	if request.method == "POST":

		form =  Shop_Form(request.POST)

		if form.is_valid():

			form.instance.owner = owner
			form.save()
			shop_slug = form.instance.slug

			return redirect(reverse("shops:detail-shop", kwargs={"shop_slug": shop_slug}))

	return render(request, "shops/create_shop.html", {"form":form})

def detail_shop_view(request, shop_slug):

	shop = None 
	products = []
	profile = None
	if request.user.is_authenticated:
		profile = get_object_or_404(Profile, user=request.user)

	if shop_slug:

		shop = Shop.objects.get(slug=shop_slug)
		products = Product.objects.all().filter(available=True, shop=shop)

	return render(request, "shops/detail_shop.html", {"shop": shop, "products": products, "profile":profile})

def list_shop_view(request):

	shops = Shop.objects.all()
	

	return render(request, "shops/list_shop.html", {"shops": shops})

def create_product_view(request):

	form = Product_Form()
	profile = get_object_or_404(Profile, user=request.user)
	shop = Shop.objects.get(owner=profile)

	if request.method == "POST":

		form = Product_Form(request.POST, request.FILES)
		print(request.FILES)

		if form.is_valid():
			image = request.FILES["image"]
			form.instance.image = image
			form.instance.seller = shop.owner
			form.instance.available = True
			form.instance.shop = shop

			form.save()

			return redirect(reverse("shops:detail-shop", kwargs={"shop_slug": form.instance.shop.slug})) #redirect somewhere

	return render(request, "product/product_creation.html", {"form": form, "shop":shop})


def detail_product_view(request, shop_slug, slug):

	shop = get_object_or_404(Shop, slug=shop_slug)
	cart = Shopping_Cart(request)

	if shop_slug and slug:

		product = Product.objects.get(slug=slug, shop=shop)
		
		if request.method == "POST":

			cart.add_product(product.id) 

	return render(request, "product/product_detail.html", {"product": product}) 

def update_product_view(request, shop_slug, slug):

	shop = get_object_or_404(Shop, slug=shop_slug)
	product_object = Product.objects.get(slug=slug, shop=shop)
	form = Product_Form(request.POST or None, instance=product_object)

	if request.method == "POST":

		if form.is_valid():

			form.save()

			return redirect(product_object)

	return render(request, "product/product_update.html", {"form": form, "product": product_object})

def delete_product_view(request, shop_slug, slug):

	shop = get_object_or_404(Shop, slug=shop_slug)
	product_object = Product.objects.get(slug=slug, shop=shop)

	if request.method == "POST":

		product_object.delete()

		return redirect(reverse("shops:detail-shop", kwargs={"shop_slug": shop.slug}))

	return render(request, "product/product_delete.html", {"shop":shop, "product":product_object})

def shop_list_view(request):

	cart = Shopping_Cart(request)
	products = cart.create_products_list()
	customer = None
	if request.user.is_authenticated:
		customer = get_object_or_404(Profile, user=request.user)

	if request.method == "POST":

		#panier = literal_eval(request.POST["panier"])
		print(request.POST)
		try:

			id = request.POST["Delete"]
			product = Product.objects.get(id=int(id))
			cart.remove_product(product, products)
			request.session.save()

		except KeyError as e:
			pass

		if request.POST["panier"] != "order":

			panier = cart.deserialize_json(request.POST["panier"])
			random_address = Address.objects.create(country="BE", city="some city", 
														street="a street", postal_code=1000)
			order = Order(paid=False, address=random_address, customer=customer, shoplist=panier)
			order.save()
			cart.clear_shopping(products)
			order_creation.send(sender=Order, user=customer, order=order)
		print(request.session["shopping_cart"])

	total_prices = cart.get_total_price()
		
	return render(request, "shops/shoplist.html", {"products": products, "total_cost": total_prices})


def products_list_View(request):

	products = Product.objects.all()

	return render(request, "product/productList.html", {"products":products})