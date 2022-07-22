from django.urls import path
from .views import books,signup,signin,signout


urlpatterns = [
    path("books/", books, name="books"),
    path("books/signup/", signup, name="signup"),
    path("books/signin/", signin, name="login"),
    path("books/signout/", signout, name="logout"),
]

