from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()
class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =(
            'email',
            'username',
            'first_name',
            'last_name'
   
   
     )
#create my own form
from django import forms

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ["username","password"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "ml-5 inline-flex items-center bg-gray-100 border-0",
                    "placeholder": "your@email.com"
                    }), 
            # "username_label": forms.TextInput(
            #     attrs={
            #         "class": "block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2",
            #         }), 
            "password": forms.PasswordInput(
                attrs={
                    "class": "shadow-sm rounded-md w-full px-3 py-2 border border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
                    }),
            # "password_label": forms.PasswordInput(
            #     attrs={
            #         "class": "block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
            #         })
            }