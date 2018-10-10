from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name','image_url', 'brand','description', 'status' ,'price', 'sales_price',  )