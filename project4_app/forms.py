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
		widgets = {
		"description": forms.Textarea(
			attrs={
			"placeholder": "Product Description"
			}
			),
		"name": forms.TextInput(
			attrs={
			"placeholder": "Product Name"
			})
		}
