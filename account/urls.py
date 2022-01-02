from django.urls import path
from .views import RegisterUser, login_user

app_name = 'account'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', login_user, name='login'),
]
