from django.urls import path
from .views import*
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("books/", books, name="books"),
    path("signup/", signup, name="signup"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),  
    path("profile", UserProfile, name="profile"),
    path("signout", UserLogout, name="signout"),
    path("signin", UserLogin, name="signin"),
    path('password', UserChangePassword, name='change_password'),
    # path("books/signout/", signout, name="logout"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

]
