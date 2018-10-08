from django.urls import path
from . import views

urlpatterns = [
	path('products/<int:pk>', views.details_product, name="details_product"),
	path('products', views.list_product, name="list_product"),
]