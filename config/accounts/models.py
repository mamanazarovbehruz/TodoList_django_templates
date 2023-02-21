from django.db import models
from django.contrib.auth.models import AbstractUser
# from company.models import Company, Department

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account/', blank=True, null=True)
    company = models.ForeignKey('company.Company', related_name='workers', blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('company.Department', related_name='workers', blank=True, null=True, on_delete=models.SET_NULL)
    tel = models.CharField(max_length=14, blank=True, null=True)