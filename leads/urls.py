from django.urls import path
from .import views

urlpatterns = [
    path ('landing' , views.landing.as_view(), name='landing'),
    path('', views.Create_lead.as_view(), name='create_lead'),
    path('lead_list/',views.lead_list.as_view() , name="lead_list"),
    path('lead_list/<int:id>',views.lead_detail.as_view(), name='lead_detail'),
    path('Update_lead/<int:id>', views.Update_lead.as_view(), name='update_lead'),
    path('lead_delete/<int:id>', views.lead_delete.as_view(), name='lead_delete'),
    path('LoggedOut', views.LoggedOutview.as_view(), name="logged_out")
   

]
