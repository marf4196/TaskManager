from django.urls import path
from home import views

app_name='main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
]
