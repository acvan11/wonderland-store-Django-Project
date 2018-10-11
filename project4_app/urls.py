from django.urls import path
from . import views

urlpatterns = [
	path('', views.product_list, name="product_list"),
	path('products/<int:pk>', views.product_detail, name="product_detail"),
	path('products/<int:pk>/edit', views.product_edit, name="product_edit"),
	path('products/new', views.product_create, name="product_create"),
	path('products/<int:pk>/delete', views.product_delete, name="product_delete"),
	path('signup', views.signup, name="signup"),
	path('login', views.login, name="login"),
	path('logout', views.logout, name="logout"),
	path('cart', views.cart, name='cart'),
	path('cart/<int:pk>/remove', views.cart_remove, name="cart_remove"),
	]