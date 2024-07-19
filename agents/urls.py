from django.urls import path
from . import views 
app_name= 'agents'
urlpatterns = [
    path('agent',views.agent_list.as_view() , name="agent_list"),
    path('create', views.AgntCreateView.as_view(), name='create_agent'),
    path('agent/<int:pk>',views.Agent_detail.as_view(), name='agent_detail'),
    path('Agent_update/<int:id>', views.Agent_update.as_view(), name='agent_update'),
    path('agent_delete/<int:pk>', views.agent_delete.as_view(), name= 'agent_delete'),
    path('Agentlist',views.Agentlist.as_view() , name="Agentlist"),


   

    
]
