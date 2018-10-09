from django.shortcuts import render
from .models import Product

# Create your views here.

from .forms import ProductAddForm

# detail of one item

def create_view(request):

	form = ProductAddForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		name = data.get("name")
		description = data.get("description")
		price = data.get("price")
		new_obj = Product()
		new_obj.name = name
		new_obj.description = description
		new_obj.price = price
		new_obj.save()
	return render(request, "create_view.html", {"form" : form})

def details_product(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "details.html", {'product' : product})

# list of all products
def list_product(request):
	products = Product.objects.all()
	return render(request, "list_products.html", {"products" : products})