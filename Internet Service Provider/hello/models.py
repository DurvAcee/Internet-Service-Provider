from djongo import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class User(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    pwd = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name

class Payment(models.Model):
    owner = models.CharField(max_length=122)
    card_num = models.CharField(max_length=20)
    exp_year = models.CharField(max_length=5)
    exp_month = models.CharField(max_length=3)
    cvv = models.CharField(max_length=4)
    email=models.CharField(max_length=122)
    planid=models.CharField(max_length=5)
    accno = models.CharField(max_length=20)
    mob = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.owner


class Plan(models.Model):
    price = models.CharField(max_length=122)
    validity = models.CharField(max_length=122)
    speed=models.CharField(max_length=122)
    data = models.CharField(max_length=100)
    subsc = models.TextField()

    def _str_(self):
        return self.price


class Checkout(models.Model):
    accno = models.CharField(max_length=122)
    regno = models.CharField(max_length=122)

    def _str_(self):
        return self.regno






