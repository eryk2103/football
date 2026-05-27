from django.urls import path
from standings import views

urlpatterns = [
    path('', views.index, name='standings_index'),
]
