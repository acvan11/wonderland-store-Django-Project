from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	# show column description, price, sales_price on admin sites
	list_display = ["__str__", "description", "price", "sales_price"]
	# have a search bar that search the name or description
	search_fields = ["name", "description"]
	# have a filter bar at the right side
	list_filter = ["price", "sales_price"]
	# we could edit the sales_price and price 
	list_editable = ["sales_price", "price"]
	
	class Meta:
		model = Product

# Register your models here.
admin.site.register(Product, ProductAdmin)