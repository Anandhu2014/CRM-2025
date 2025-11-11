from django.db import models

# Create your models here.

from students.models import BaseClass

# Create your models here.

class Trainer(BaseClass):
    
    name =models.CharField(max_length=15)
    
    class Meta:
        
        verbose_name ='Trainers'
        
        verbose_name_plural ='Trainers'
        
    def __str__(self):
        
        return self.name
