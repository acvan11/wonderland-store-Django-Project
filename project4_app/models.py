from django.db import models
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField(null=True)
	sales_price = models.FloatField(null=True)
	status = models.CharField(max_length=100, null=True)
	brand = models.CharField(max_length=100, null=True)
	image_url = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name
