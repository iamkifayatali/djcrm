from django.shortcuts import render , reverse , redirect , HttpResponseRedirect
from django.http import HttpResponse
from .models import Lead
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import LeadForm , CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixens import OrganisiorAndLoginRequireMixin
from django.contrib.auth.views import  LogoutView
from django.contrib import messages
from django.contrib.auth import logout as auth_logout


from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to the homepage
        return super().get(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse('logged_out')
    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, "You are successfully Logout!")
        auth_logout(request)
        # return super(CustomLogoutView).post(self, request, *args, **kwargs )
        return redirect(self.get_success_url())

        

class LoggedOutview(generic.TemplateView):
    template_name="leads/logged_out.html"



class SignUpView(generic.CreateView):
    template_name="registration/signup.html"
    form_class =CustomUserCreationForm

    def get(self, request, *args, **kwargs ):
        # print(request.user)
        # print(request.user.id)
        # print(reverse("lead_list"))
        if request.user.id:
         
           return redirect( reverse("lead_list"))
        else:
           
            return super().get(self, request, *args, **kwargs)
            
          
    
    
            

    def get_success_url(self):
        return reverse ("login")

class  landing(generic.TemplateView):
    template_name='landing.html'

class Create_lead(OrganisiorAndLoginRequireMixin,generic.CreateView):
   model= Lead
   fields= '__all__' 
   template_name='leads/create_lead.html'
   success_url = ('/LeadList')
  
class lead_list(LoginRequiredMixin, generic.ListView):
    template_name="leads/lead_list.html"
    context_object_name='lead'
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile , agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        return queryset
    def get_context_data(self , **kwargs):
        user=self.request.user
        context = super(lead_list, self).get_context_data(**kwargs)
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                  agent__isnull=True)
        context.update(
            {
                "unassinged_leads":queryset
            }
        )
        return context


    def lead_list(request):
        leads = leads.objects.al()
        context ={
            "leads": leads
        }
        return render(request,"leads/lead_list.html", context)


class lead_detail(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    def get_object(self, queryset=None):
        return Lead.objects.get(id=self.kwargs['id'])
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset

class Update_lead(OrganisiorAndLoginRequireMixin, generic.UpdateView):
    fields = '__all__'  
    template_name='leads/update_lead.html'
    success_url = reverse_lazy('lead_list')  
    def get_object(self, queryset=None):
        return Lead.objects.get(id=self.kwargs['id'])
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset
      
class lead_delete(OrganisiorAndLoginRequireMixin,generic.DeleteView):
    template_name='leads/delete_confirm.html'
    success_url = reverse_lazy('lead_list')
    def get_object(self, queryset=None):
         return Lead.objects.get(id=self.kwargs['id'])
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset
#creating my own form
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('landing')
    template_name = 'leads/change_password.html'


class  LeadList(generic.TemplateView):
    template_name="leads/leadlist.html"
    # context_object_name='lead'
    def get_queryset(self):
        user=self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organisation=user.userprofile , agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        return queryset
    def get_context_data(self , **kwargs):
        user=self.request.user
        context = super(LeadList, self).get_context_data(**kwargs)
        if user.is_organizer:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                  agent__isnull=True)
        context.update(
            {
                "unassinged_leads":queryset
            }
        )
        context['leads'] = self.get_queryset()

        return context


    def lead_list(request):
        leads = leads.objects.all()
        context ={
            "leads": leads
        }
        return render(request,"leads/leadlist.html", context)

