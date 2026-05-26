from django.urls import path

from matches import views

urlpatterns = [
    path('index', views.index, name='matches_index'),
    path('<int:pk>', views.show, name='matches_show'),
]
