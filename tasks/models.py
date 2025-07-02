from django.db import models
from django.contrib.auth.models import User
#Import defult model User from django(its fielsd are:name,email, password)

# Create your models here.
class Tasks(models.Model):
    title =            models.CharField(max_length=50)
    owner =            models.ForeignKey(User, on_delete=models.CASCADE)# Defult code for ManyToOne Realchinship
    description =      models.TextField(blank=True)#Blank (جعل الحقل اختياري) makes the user late it empty or not/without input  
    is_completed =     models.BooleanField(default=False)
    created_at =       models.DateTimeField(auto_now_add=True)
    due_date  =        models.DateTimeField(null=True, blank=True)

