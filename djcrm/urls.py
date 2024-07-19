
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView ,LogoutView ,PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
from django.urls import path , include
from leads.views import landing , SignUpView , ChangePasswordView, CustomLogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing', landing.as_view(), name='landing-page'),
    path('', include('leads.urls')),
    path('agents/', include('agents.urls')),
    path('Users', include('Users.urls')),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', CustomLogoutView.as_view(), name='logout'),
    path('resetpassword' , PasswordResetView.as_view(), name='resetpassword'),
    path('password_reset_done' , PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password_reset_complete' , PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('SignUp', SignUpView.as_view(), name='SignUpView'),
    path('change-password',ChangePasswordView.as_view(), name='change_password'),
    # path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

