from django.db.models.query import QuerySet
from django.shortcuts import render , reverse
from django.http import HttpResponse
from leads.models import Agent ,Lead, UserProfile
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AgentModelForm
from .mixens import OrganisiorAndLoginRequireMixin 
import random

class agent_list( OrganisiorAndLoginRequireMixin, generic.ListView):
    template_name='agent/agent_list.html'
    context_object_name='agent'
    def get_queryset(self):
        organisation= self.request.user.id
        return Agent.objects.filter(organisation=organisation)
        # our_user = UserProfile.objects.get(user=form.instance.user.id)
        # organisation = our_user
        return Agent.objects.filter(organisation=organisation)
        
        

class Agentlist(OrganisiorAndLoginRequireMixin, generic.ListView):
    template_name='agent/agentlist.html'
    context_object_name='agent'
    def get_queryset(self):
        organisation= self.request.user.id
        return Agent.objects.filter(organisation=organisation)
        # our_user = UserProfile.objects.get(user=form.instance.user.id)
        # organisation = our_user
        return Agent.objects.filter(organisation=organisation)
        
class AgntCreateView(OrganisiorAndLoginRequireMixin, generic.CreateView):
   template_name='agent/create_agent.html'
   form_class = AgentModelForm
   def get_success_url(self):
       return reverse("agents:Agentlist")
   def  form_valid(self, form):
       user = form.save(commit=False)
       user.is_agent = True
       user.is_organizer = False
       user.set_password(f"{random.randint(0,100000)}")
       user.save()
       Agent.objects.create(
           user=user,
           organisation = self.request.user.userprofile
       )
       send_mail(
           subject="you are invites to be an agent",
           message="you were added as an agent on DJcrm, please login to start working",
           from_email="admin@test.com",
           recipient_list=[user.email]
       )
    #    agent = form.save(commit=False)
    #    our_user = UserProfile.objects.get(user=form.instance.user.id)
      

    #    agent.organisation = our_user
    #    agent.save()
       return super(AgntCreateView, self).form_valid(form)
   


class Agent_detail(OrganisiorAndLoginRequireMixin, generic.DetailView):
    template_name = "agent/agent_detail.html"
    context_object_name='agent'
    def get_queryset(self):
        organisation= self.request.user.id
        print(organisation)
        return Agent.objects.filter(organisation=organisation)

class Agent_update(OrganisiorAndLoginRequireMixin, generic.UpdateView):
    model = Agent 
    fields = '__all__'  
    template_name='agent/agent_update.html'
    success_url = reverse_lazy('agents:agent_list')  
    def get_object(self, queryset=None):
        return Agent.objects.get(id=self.kwargs['id'])

      
class agent_delete(OrganisiorAndLoginRequireMixin, generic.DeleteView):
   
    template_name='agent/confirm_delete.html'
    context_object_name='agent'
    success_url = reverse_lazy('agents:agent_list')
    def get_queryset(self):
        organisation= self.request.user.id
        return Agent.objects.filter(organisation=organisation)
    

