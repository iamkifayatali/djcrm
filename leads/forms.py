from django import forms 
from django.contrib.auth import get_user_model,password_validation
from django.contrib.auth.forms import UserCreationForm , UsernameField , UserChangeForm
from .models import User , Lead
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class LeadForm(forms.ModelForm):
    class Meta:  
          
        model = Lead
        # model = Agent  
        
        fields = '__all__'  

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","placeholder":"password","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","placeholder":"password again","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
     )
    first_name = forms.CharField(
        label=_("FirstName"),
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder":"Firstname","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    last_name = forms.CharField(
        label=_("LastName"),
        widget=forms.PasswordInput(attrs={"placeholder":"LastName","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}),
        strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
     )
    class Meta:
        model = User
         
        fields = ['email',
            'username',
            'first_name',
            'last_name']
        field_classes = {"username": UsernameField}

    email = forms.CharField(
        label=_("Email"),
        widget=forms.PasswordInput(attrs={"type":"email","class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500","placeholder":"Your email"}),
        strip=False,
        # help_text=_("please enter your email"),
     )

    username = forms.CharField(
        label=_("username"),
        widget=forms.PasswordInput(attrs={"class":"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500","placeholder":"Unique Username"}),
        strip=False,
    #     help_text=_("Enter the same password as before, for verification."),
     )

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        username = cleaned_data.get('username')
        if  username.startswith("0") or username.startswith("1") or username.startswith("2")or username.startswith("3")or username.startswith("4")or username.startswith("5") or  username.startswith("6") or username.startswith("7")or username.startswith("8")or username.startswith("9") :
            self.add_error('username', 'numbers  are not allowed in the start of username.')
       
        return cleaned_data
    
class CustomUserCreationFormForUpdate(forms.ModelForm):
    class Meta:
        model = User
            
        fields = ['username',
                'email',
                'first_name',
                'last_name']
        field_classes = {"username": UsernameField}
        def clean(self):
            cleaned_data = super(CustomUserCreationFormForUpdate, self).clean()
            username = cleaned_data.get('username')
            if  username.startswith("0") or username.startswith("1") or username.startswith("2")or username.startswith("3")or username.startswith("4")or username.startswith("5") or  username.startswith("6") or username.startswith("7")or username.startswith("8")or username.startswith("9") :
                self.add_error('username', 'numbers  are not allowed in the start of username.')
            return cleaned_data