from django.urls import path
from . import views 
app_name= 'Users'
urlpatterns = [
   
    path('Users/<int:pk>',views.User_detail.as_view(), name='User_detail'),
    path('user_delete/<int:pk>', views.User_delete.as_view(), name= 'user_delete'),
    path('user_update/<int:pk>', views.User_update.as_view(), name='user_update'),

    
]
