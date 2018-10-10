from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {'products': products})


def edit_product(request, pk):
	product = Product.objects.get(id=pk)
	form = ProductModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.sales_price = instance.price 
		instance.save()
	return render(request,"edit_product.html", {"form": form})


def details_product(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "details.html", {'product' : product})

# list of all products
def list_product(request):
	products = Product.objects.all()
	return render(request, "list_products.html", {"products" : products})








