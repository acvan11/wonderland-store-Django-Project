from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "product_detail.html", {'product' : product})

def product_edit(request, pk):
	products = Product.objects.get(id=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			product = form.save()
			return redirect('product_detail', pk=product.pk)
	else:
		form = ProductForm(instance=product)
		return render(request, 'product_new.html', {'form': form})



# list of all products
def list_product(request):
	products = Product.objects.all()
	return render(request, "list_products.html", {"products" : products})








