from django.shortcuts import render
from .models import Product

# Create your views here.

from .forms import ProductAddForm, ProductModelForm


# detail of one item

def create_view(request):

	form = ProductModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.sales_price = instance.price 
		instance.save()

	return render(request, "create_view.html", {"form" : form})

def details_product(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "details.html", {'product' : product})

# list of all products
def list_product(request):
	products = Product.objects.all()
	return render(request, "list_products.html", {"products" : products})