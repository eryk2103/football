from django.shortcuts import render
from .models import Team


def index(request):
    teams = Team.objects.select_related('country', 'stadium').order_by('name')
    return render(request, 'teams/index.html', {'teams': teams})
