from django import forms

class ProductAddForm(forms.Form):
	name = forms.CharField()
	description = forms.CharField()
	price = forms.FloatField()