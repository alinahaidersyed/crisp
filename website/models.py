import random
from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    codehex = models.CharField(max_length=10, unique=True, default='0000000000')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Voucher(models.Model):
    voucher_number = models.CharField(max_length=10)
    is_free_umbrella = models.BooleanField(default=False)

    @classmethod
    def generate_vouchers(cls):
        # Generate 100 voucher objects
        voucher_numbers = [str(i) for i in range(1, 101)]
        random.shuffle(voucher_numbers)
        for i, voucher_number in enumerate(voucher_numbers):
            voucher = cls(voucher_number=voucher_number)
            if i == 0:
                # First voucher gets the free umbrella
                voucher.is_free_umbrella = True
            voucher.save()

    def __str__(self):
        return f"Voucher Number: {self.voucher_number}, Free Umbrella: {self.is_free_umbrella}"
