from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Create your models here.
class Files(models.Model):
    file_name = models.CharField(max_length=200)
    uploaded_file = models.FileField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner







class MetaData(models.Model):
    file_meta= models.ForeignKey(Files, blank=True, null=True,on_delete=models.CASCADE)
    file_name = models.CharField('file_name', max_length =50)
    file_size = models.CharField('file_size', max_length =50)
    file_type = models.CharField('file_type', max_length =50)
    file_extension= models.CharField('file_extension', max_length =50)
    storage_location = models.CharField('storage_location', max_length =50)
    date_created = models.CharField('date_created', max_length =50)
    date_modified = models.CharField('date_modified', max_length =50)


class Profile(models.Model):
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    first_name = models.CharField('first_name', max_length =50)
    last_name = models.CharField('last_name', max_length =50)
    email_address= models.EmailField('email_address', max_length=50)
    country =models.CharField('country', max_length=50)
    occupation =models.CharField('occupation', max_length=50)
    gender=models.CharField('gender', max_length=50)
    phone_number= models.CharField("phone_number", max_length =50)
    file_details= models.ManyToManyField(MetaData,  blank = True, null = True)
    

    def __str__(self):
        return self.user_name














