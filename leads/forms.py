from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UsernameField
from .models import User , Lead
User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:  
          
        model = Lead
        # model = Agent  
        
        fields = '__all__'  

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
         
        fields = ['email',
            'username',
            # 'password',
            'first_name',
            'last_name']
        field_classes = {"username": UsernameField}
