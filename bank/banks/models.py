from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	zip_code = models.CharField(max_length = 10)
	email = models.EmailField()
	password = models.CharField(max_length = 200)

class Account(models.Model):
	balance= models.CharField(max_length = 200)
	account_number= models.CharField(max_length= 200)
	customer= models.ForeignKey(Customer, on_delete= models.CASCADE)

class Authenticator(models.Model):
	user_id = models.CharField(max_length = 100)
	authenticator = models.CharField(max_length = 200, primary_key = True)
	date_created = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.user_id





