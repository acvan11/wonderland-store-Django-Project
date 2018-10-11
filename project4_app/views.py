from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Product, Order
from django.http import HttpResponse
from .forms import ProductForm


def product_list(request):
	products = Product.objects.all()
	return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
	product = Product.objects.get(id=pk)
	return render(request, "product_detail.html", {'product' : product})

def product_edit(request, pk):
	product = Product.objects.get(id=pk)
	if request.method == 'POST':
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			product = form.save()
			return redirect('product_detail', pk=product.pk)
	else:
		form = ProductForm(instance=product)
		return render(request, 'product_new.html', {'form': form})

def product_create(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save()
			return redirect('product_detail', pk=product.pk)
	else:
		form = ProductForm()
		return render(request, 'product_new.html', {'form': form})

def product_delete(request, pk):
	Product.objects.get(id=pk).delete()
	return redirect('product_list')

 # Auth-related routes
def signup(request):
	if request.method == 'GET':
		return render(request, 'signup.html')
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']

		try:
			user = User.objects.create_user(username=username, 
				password=password, 
				first_name = firstname,
				last_name = lastname)
			if user is not None:
				# auth.login(request, user)
				return login(request)
		except:
			return render(request, 'signup.html', { 'error': 'Arggggg!' })
		return HttpResponse('POST to /signup')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('product_list')
        else:            
            return render(request, 'login', { 'error': 'Invalid credentials' })


def logout(request):
	auth.logout(request)
	return redirect('product_list')


def cart(request):
	if request.method == 'POST':
		product = Product.objects.get(pk = request.POST['product'])
		order = Order(
				product = product,
				quantity = request.POST['quantity'],
				user_id = request.user,
			)
		order.total_price()
		order.save()
		return redirect('cart')

	if request.method == 'GET':
		total = 0
		orders = Order.objects.all().filter(user_id = request.user)
		for order in orders:
			total += order.price 
		return render(request, 'cart.html', {'orders': orders, 'total': total})

def cart_remove(request, pk):
	Order.objects.get(id=pk).delete()
	return redirect('cart')

def checkout(request):
	return render(request, 'checkout.html')

def proceed(request):
	return render(request, 'proceed.html')


