from django.db import models
import json

# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    desc=models.TextField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Contact'
    
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="")
    generic=models.CharField(max_length=100,default="")
    price=models.IntegerField(default=0)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/images",default="")
    def __str__(self):
        return self.product_name
    class Meta:
        db_table = 'Product'
    

class Orders(models.Model):
    items_json = models.JSONField()
    def get_product_info(self):
        product_info = []
        # Parse the JSON string into a Python object
        data_obj = json.loads(self.items_json)
        if isinstance(data_obj, dict):
            for key, value in data_obj.items():
                quantity, name, unit_price = value
                product_info.append({
                    'quantity': quantity,
                    'name': name,
                    'unit_price': unit_price
                })
        return product_info
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)   
    delivered = models.CharField(default="Not delivered",max_length=100)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.email
    class Meta:
        db_table = 'Orders'