from django.shortcuts import render,redirect

from .forms import LoginForm

# Create your views here.

from django.views import View

# from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages


# authenticate(username,password) it checks whether a registered email user exits it returns it ,if no then return none
# login(user) is a django fn that make the user login

class LoginView(View):
    
    form_class = LoginForm
    
    def get(self,request,*args,**kwargs):
        
        form = self.form_class()
        
        data={'form':form}
        
        return render(request,'authentication/login.html',context=data)
    
    def post(self,request,*args,**kwargs):
        
        form =self.form_class(request.POST)
        
        error = None
        
        if form.is_valid():
            
            # cleaned_data = {'email':emailvalue given by user,'password':'password given by user'}
            
            email = form.cleaned_data.get('email')
            
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=email,password=password)
            
            if user:
                
                login(request,user)
                
                messages.success(request,'successfully logined')    # to give logged in notification after successfull login
                
                return redirect('dashboard')
            
            error = 'invalid email or password'
        
        data ={'form':form,'error':error}
        
        return render(request,'authentication/login.html',context=data)
    
    
class LogoutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
        
        return redirect('login')
    
    
    
    

