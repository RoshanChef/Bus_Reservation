from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=25 , default = "1")
    def __str__(self):
        return self.name 

class author(models.Model):
    name = models.CharField(max_length=20)
    post = models.ImageField(upload_to="Images/")


class feedback(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    message = models.TextField()

class state(models.Model):  
    state = models.CharField(max_length=25)
    seats = models.IntegerField()

    def __str__(self):
        return self.state
    

class ticket(models.Model):
    email = models.EmailField()
    source = models.CharField(max_length=25)
    destination = models.CharField(max_length=25)
    numTickets = models.IntegerField()
    stateid = models.IntegerField(default=0)
    agencyid = models.IntegerField(default=0)
    price = models.IntegerField()
    orderid = models.CharField(max_length=25 , default = 0)

class bus(models.Model):
    agency = models.CharField(max_length=25)
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    agencyid = models.IntegerField(default = 0)
    busid = models.IntegerField()
    seats = models.IntegerField()
    price = models.IntegerField()
    stateid = models.IntegerField()

class agen_reg(models.Model):
    name = models.CharField(max_length=30)
    agen_name = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=25 , default = "1")
    
    def __str__(self):
        return self.name 
      
class order(models.Model):
    orderid = models.CharField(max_length=25)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    transactionid = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.orderid