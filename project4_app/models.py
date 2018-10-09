from django.db import models
from django.db.models.signal import pre_save, post_save

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.FloatField(null=True)
	sales_price = models.FloatField(null=True)

	def __str__(self):
		return self.name

def product_pre_save_reciever(sender, instance, *args, **kwargs):
	print sender
	print instance

pre_save.connect(product_pre_save_reciever, sender=Product)