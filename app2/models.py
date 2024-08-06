from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)



class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone_number=models.BigIntegerField()
    e_mail=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.BigIntegerField()


class farmer_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    phone_number=models.BigIntegerField()
    e_mail=models.CharField(max_length=100)



class product_table(models.Model):
    PRODUCT=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    rate=models.FloatField()
    image=models.FileField()
    FARMER=models.ForeignKey(login_table,on_delete=models.CASCADE)

class complaint_table(models.Model):
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product_table,on_delete=models.CASCADE)





class notification_table(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateField()


class feedback_and_rating(models.Model):
    feedback=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    date=models.DateField()
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    FARMER=models.ForeignKey(farmer_table,on_delete=models.CASCADE)


class product_rating_and_feedback(models.Model):
    feedback=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    date=models.DateField()
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(product_table,on_delete=models.CASCADE)








