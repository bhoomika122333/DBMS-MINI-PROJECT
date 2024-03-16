from django.db import models

# Create your models here.

class Bottle(models.Model):
    bottleid = models.AutoField(primary_key=True)
    brandname = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    bottledetailscol = models.CharField(max_length=45)

class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    bottle = models.ForeignKey(Bottle, on_delete=models.CASCADE)


class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    phonenumber = models.BigIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userid', 'phonenumber'], name='user_primary_key')
        ]


class Company(models.Model):
    companyid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    contactnum = models.CharField(max_length=45)
    email = models.EmailField()


class OrderAddress(models.Model):
    ordaddid = models.IntegerField(primary_key=True)
    orderid = models.IntegerField()
    addressline = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    country = models.CharField(max_length=45)



class Order(models.Model):
    orderid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    orddate = models.CharField(max_length=45)
    deliverydate = models.CharField(max_length=45)
    status = models.CharField(max_length=45)


class OrderAddress(models.Model):
    ordaddid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    orderaddcol = models.CharField(max_length=45)



class Bottle(models.Model):
    bottleid = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price = models.CharField(max_length=45)
    stock = models.CharField(max_length=45)



class UserDetails(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
