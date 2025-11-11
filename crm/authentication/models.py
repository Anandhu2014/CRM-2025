from django.db import models

from django.contrib.auth.models import AbstractUser 

from students.models import BaseClass  

# Create your models here.

#for creating our own users and roles instead of django default user

class RoleChoices(models.TextChoices):
    
    ADMIN = 'Admin','Admin'
    
    STUDENT = 'Student','Student'
    
    Trainer = 'Trainer','Trainer'
    
    SALES = 'Sales','Sales'
    
    ACADEMIC_COUNSELLOR = 'Academic Counsellor','Academic Counsellor'

class Profile(AbstractUser):
    
    role = models.CharField(max_length=25,choices=RoleChoices.choices)
    
    
    class Meta:
        
        verbose_name = 'Profiles'
        
        verbose_name_plural = 'Profiles'
        
    def __str__(self):
        
        return self.username
    
class OTP(BaseClass):
    
    profile = models.OneToOneField('Profile',on_delete=models.CASCADE)
    
    email_otp = models.CharField(max_length=4,null=True,blank=True)
    
    phone_otp = models.CharField(max_length=4,null=True,blank=True)
    
    otp_verified = models.BooleanField(default=False)
     
    class Meta:
        
        verbose_name = 'OTPs'
        
        verbose_name_plural = 'OTPs'
        
    def __str__(self):
        
        return f'{self.profile.username} OTP'
        
    
    