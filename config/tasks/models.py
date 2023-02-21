from django.db import models
from accounts.models import *
from company.models import *

# Create your models here.

class Task(models.Model):

    PRIORITY_CHOICE = (
        ('low', 'LOW'),
        ('middle', 'MIDDLE'),
        ('hight', 'HIGHT'),
    )
    STATUS_CHOICE = (
        ('upcoming', 'UPCOMING'),
        ('overcoming', 'OVERCOMING'),
        ('expired', 'EXPIRED'),  
        ('rejected', 'REJECTED'),
        ('active', 'ACTIVE'),
        ('complated', 'COMLATED'),
        ('archive', 'ARCHIVE'),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    company = models.ForeignKey(Company, related_name='tasks', blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, related_name='tasks', blank=True, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(User, related_name='tasks')
    project = models.ForeignKey(Project, related_name='tasks', blank=True, null=True, on_delete=models.SET_NULL)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICE, default='middle')
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='upcoming')
    
    def __str__(self):
        return self.title
    
class Task_image(models.Model):
    task = models.ForeignKey(Task,related_name='images', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='taskimage/')

class Task_file(models.Model):
    task = models.ForeignKey(Task,related_name='files', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='taskfile/', blank=True, null=True)

class Task_item(models.Model): 
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, related_name='taskitem', blank=True, null=True, on_delete=models.SET_NULL)
    members = models.ManyToManyField(User)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comment', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, related_name='comment', blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='comment/', blank=True, null=True)
    body = models.TextField()
    reply = models.ForeignKey('self', related_name='child', blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
