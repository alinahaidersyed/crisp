from django.db import models


class Record(models.Model):
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	address =  models.CharField(max_length=100)
	codehex = models.CharField(max_length=10,default='0000000000')
	

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class Voucher(models.Model):
    code = models.CharField(max_length=10, unique=True)
    voucher_number = models.CharField(max_length=10)
    is_free_umbrella = models.BooleanField(default=False)

    def __str__(self):
        return f"Code: {self.code}, Voucher: {self.voucher_number}"