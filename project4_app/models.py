from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User


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

class Order(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
	quantity = models.IntegerField()
	price = models.FloatField(default = 0)


	def total_price(self):
		self.price = int(self.product.sales_price) * int(self.quantity)


	def __str__(self):
		return str(self.price)