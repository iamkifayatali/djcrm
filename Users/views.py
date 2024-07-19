from django.shortcuts import render , reverse , redirect , HttpResponseRedirect
from django.http import HttpResponse
from leads.models import User
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from leads.forms import LeadForm , CustomUserCreationFormForUpdate
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixens import OrganisiorAndLoginRequireMixin



        





class User_detail( generic.DetailView):
    model=User
    template_name = "Users/Users_detail.html"
    context_object_name="user"

    
class User_update(OrganisiorAndLoginRequireMixin, generic.UpdateView):
    model = User 
    form_class =CustomUserCreationFormForUpdate

    template_name='Users/user_update.html'
    def get_success_url(self):
        return reverse_lazy('Users:User_detail', kwargs={'pk': self.request.user.id})


      
class User_delete(OrganisiorAndLoginRequireMixin,generic.DeleteView):
    model= User
    template_name='Users/delete_confirm.html'
    context_object_name="user"
    success_url = reverse_lazy('landing')





