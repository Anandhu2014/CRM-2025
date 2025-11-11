from django import forms

from .models import Students,EducationChoices,DistrictChoices,CourseChoices,BatchChoices,TrainerChoices

import re

from course.models import Course

from batch.models import Batch

from trainer.models import Trainer

class AddStudentForm(forms.ModelForm):
    
    class Meta :
        
        model = Students
        
        # fields is uded to add all fields in the model eg: fields[f_name,l_name,....].it is used if all fields are get from form
        # for getting all fields        fields ='__all__'
        
        # exclude used to excluding any field
        
        exclude = ['join_date','adm_num','uuid','active_status','profile']
        
        # widgets are used to applying styles ,placeholders etc for fields.it is dictionary type
        
        widgets = { 
                    'first_name' : forms.TextInput(attrs={'class':'form-control'}),
                    
                    'last_name' : forms.TextInput(attrs={'class':'form-control'}),
                    
                    'email' : forms.EmailInput(attrs={'class':'form-control'}),
                    
                    'contact_num' : forms.TextInput(attrs={'class':'form-control'}),
                    
                    'photo' : forms.FileInput(attrs={'class':'form-control'}),
                    
                    'dob' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                    
                    'address' : forms.TextInput(attrs={'class':'form-control'}),
                    
                    'place' : forms.TextInput(attrs={'class':'form-control'}),
                    
                    'pincode' : forms.TextInput(attrs={'class':'form-control'}),
            
        }
    
    education = forms.ChoiceField(choices=EducationChoices.choices,widget=forms.Select(attrs={'class':'form-select'}))
    
    district = forms.ChoiceField(choices=DistrictChoices.choices,widget=forms.Select(attrs={'class':'form-select'}))  
      
    course = forms.ModelChoiceField(queryset=Course.objects.all(),widget=forms.Select(attrs={'class':'form-select'})) 
       
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(),widget=forms.Select(attrs={'class':'form-select'}))  
      
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.all(),widget=forms.Select(attrs={'class':'form-select'}))    
    
    def clean(self):
        
        cleaned_data = super().clean()
        
        # print(cleaned_data)
        
        pincode = cleaned_data.get('pincode')
        
        email = cleaned_data.get('email')
        
        contact_num = cleaned_data.get('contact_num')
        
        if len(pincode) < 6 :
            
            self.add_error('pincode','pincode must be 6 digits')
            
         # and not self.instance is used to avoid email change issue during form editing
        if Students.objects.filter(email=email).exists() and not self.instance:
            
            self.add_error('email','this email already taken')
            
       
        
        username,domain =email.split('@')
        
        domain_list= ["gmail.com","yahoo.com","outlook.com","hotmail.com","icloud.com","aol.com","protonmail.com","zoho.com","yandex.com","mail.com","mailinator.com"]
        
        if domain not in domain_list:
            
            self.add_error('email','invalid email address')
            
         # and not self.instance is used to avoid phone number change issue during form editing
        if Students.objects.filter(contact_num=contact_num).exists() and not self.instance:
            
            self.add_error('contact_num','this contact number already exists')
            
            
        pattern = '(\\+91)?\\d{10}'
            
        match = re.fullmatch(pattern,contact_num)
            
        if not match:
                
            self.add_error('contact_num','this phone number is not valid')
            
    
    # for solving email and phone no required issue during editing the form        
    # def __init__(self,*args,**kwargs):
        
    #     super(AddStudentForm,self).__init__(*args,**kwargs)
        
    #     if not self.instance :
            
    #         # attrs is in dictionary format .so for adding something to it give the key and value as ['key']=value
    #         self.fields.get('email').widget.attrs['required']='required'
            
        
        