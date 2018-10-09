from django import forms
from .models import Product

class ProductAddForm(forms.Form):
	name = forms.CharField(label="Product Name", widget=forms.TextInput(
		attrs={
			"class": "custom-class",
			"placeholder": "Product Name",
		}))
	description = forms.CharField(widget=forms.Textarea(
		attrs ={
			"class": "my-custom-class",
			"placeholder": "Product Description",
			"some-attr": "this",
		}))
	price = forms.FloatField()

class ProductModelForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
		"name",
		"description",
		"price"
		]


"""
name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField(null=True)
	sales_price = models.FloatField(null=True)
"""