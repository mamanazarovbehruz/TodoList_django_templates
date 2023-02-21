from django.db import models
from accounts.models import User
from uuid import uuid4

# Create your models here.

class Company(models.Model):
    owner = models.OneToOneField(User, related_name='selfcomp', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, default='company1')
    slug = models.SlugField(max_length=150, unique=True)
    logo = models.ImageField(upload_to='company', blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = f"{uuid4()}{self.title}"
        super().save(*args, **kwargs)

class Department(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    info = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name='departments', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    info = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company,related_name='projects', blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='projects', blank=True, null=True)
    tz = models.FileField(upload_to='projects', blank=True, null=True)
    department = models.ManyToManyField(Department, related_name='projects')

    def __str__(self):
        return self.title