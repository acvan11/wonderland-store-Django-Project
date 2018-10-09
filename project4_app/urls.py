from django.urls import path
from . import views

urlpatterns = [
	path('products/<int:pk>', views.details_product, name="details_product"),
	path('products', views.list_product, name="list_product"),
	path('create', views.create_view, name="create_view"),
]