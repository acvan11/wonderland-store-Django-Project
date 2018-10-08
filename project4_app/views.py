from django.shortcuts import render
from .models import Product

# Create your views here.
# detail of one item
def details_product(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "details.html", {'product' : product})

# list of all products
def list_product(request):
	products = Product.objects.all()
	return render(request, "list_products.html", {"products" : products})