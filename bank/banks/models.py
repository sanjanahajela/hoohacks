from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	zip_code = models.CharField(max_length = 10)
	email = models.EmailField()

class Account(models.Model):
	balance= models.CharField(max_length = 200)
	account_number= models.CharField(max_length= 200)
	customer= models.ForeignKey(Customer, on_delete= models.CASCADE)





