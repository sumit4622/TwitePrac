from django.urls import path
from .views import sumit

urlpatterns = [
    path('', sumit),
]
