from django.urls import path
from .views import*


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("books/", books, name="books"),
    path("register", UserRegister, name="signup"),
    path("profile", UserProfile, name="profile"),
    path("signout", UserLogout, name="signout"),
    path("signin", UserLogin, name="signin"),
    path('password', UserChangePassword, name='change_password'),
    # path("books/signout/", signout, name="logout"),
]
