from django.db import models

# Create your models here.

class profile(models.Model):
	name = models.CharField(max_length = 120)
	description = models.TextField(default = 'Enter Description here...')

	def __unicode__(self):
		return self.name

class Product(models.Model):
	product_id = models.AutoField
	product_name = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50, default = "")
	price = models.IntegerField(default=0)
	desc = models.TextField(default = '')

	def __str__(self):
		return self.product_name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
