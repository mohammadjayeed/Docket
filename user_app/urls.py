from django.urls import path,include
from .views import registration
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/',registration,name="registration_todo"),
    path('login/',LoginView.as_view(template_name="login.html"),name="login_todo"),
    path('logout/',LogoutView.as_view(template_name="logout.html"),name="logout_todo"),

]