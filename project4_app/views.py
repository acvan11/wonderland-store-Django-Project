from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Product
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
		return render(request, 'project4_app/signup.html')
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
			return render(request, 'project4_app/signup.html', { 'error': 'Arggggg!' })
		return HttpResponse('POST to /signup')

def login(request):
	if request.method == 'GET':
		return render(request, 'project4_app/login.html')
	elif request.method == 'POST':
		return HttpResponse('posignup')
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('index')
		else:            
			return render(request, 'project4_app/login.html', { 'error': 'Invalid credentials' })

def logout(request):
	return HttpResponse('logout')
	auth.logout(request)
	return redirect('index')

