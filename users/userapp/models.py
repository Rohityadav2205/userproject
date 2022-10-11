from django.db import models

# Create your models here.
class UsersModel(models.Model):
    Name=models.CharField(max_length=200)
    Photos=models.ImageField(upload_to="static/")
    Email_id=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Mobile_number=models.CharField(max_length=10)
    Date_of_birth=models.DateField(max_length=200)

def __str__():
    return "name={0},photos={1},email_id{2},password={3},mobile_number={4},date_of_birth={5}".format(self.name,self.photos,self.email_id,self.password,self.mobile_number,self.date_of_birth)

