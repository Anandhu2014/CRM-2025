# Library() - it is used for creating custom template tags.it is in django.templates

from django.template import Library

register = Library() #object created


@register.simple_tag        #decorator is applied.simple_tag is a method in library .for calling it we use the object register
def display_name(name):
    
    return name.upper()


#   it is used in html page
# {% display_name 'Anandhu' as name %}  
# {{name}}                            

@register.simple_tag 
def check_roles(request,roles):
    
    roles = roles.split(',')
    
    if request.user.is_authenticated and request.user.role in roles :
        
        return True
    
    return False