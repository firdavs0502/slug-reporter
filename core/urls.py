from django.urls import path
from .views import reporter , detal

urlpatterns = [
    path('', reporter),
    path('<slug:slug>/', detal, name='detal'),
]