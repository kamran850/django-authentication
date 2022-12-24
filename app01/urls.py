from django.urls import path
from .views import*


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("books/", books, name="books"),
    path("register", signup, name="signup"),
    path("profile", profile, name="profile"),
    path("signout", signout, name="signout"),
    path("signin", signin, name="signin"),
    # path("books/signout/", signout, name="logout"),
]
