from django.urls import path
from . import views

urlpatterns = [
    path('company/login/', views.sign_in, name='sign_in'),
]
