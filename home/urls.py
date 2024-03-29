from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path("", views.index, name="index"),
    path("viewsub/<str:filess>", views.viewsub, name="viewsub"),
    path("profile/<str:email>", views.profile_page, name = "profile_page"),
    path("conference/<str:email>", views.conference_page, name="conference_page"),
    path("conferencesubs/<str:con_namee>", views.conferencesubs_page, name="conferencesubs_page"),
    path("submissions/<str:email>", views.submissions_page, name="submissions_page"),
    path("login", views.login_page, name="login_page"),
    path("signup", views.signup_page, name="signup_page"),
  
]