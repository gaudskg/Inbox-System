from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('inbox/',views.inbox, name="inbox"),
    path('login/',views.login, name="login")

]
