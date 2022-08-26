from django.urls import path
from download_data import views


urlpatterns = [
    path('', views.index, name="Home")
]