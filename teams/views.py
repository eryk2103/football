from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Team
from competitions.models import Competition


def index(request):
    competitions = Competition.objects.order_by('name')
    competition_id = request.GET.get('competition')

    teams = Team.objects.select_related('country', 'stadium').order_by('name')

    if competition_id:
        teams = teams.filter(
            Q(home_matches__competition__competition_id=competition_id) |
            Q(away_matches__competition__competition_id=competition_id)
        ).distinct()

    paginator = Paginator(teams, 40)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'teams/index.html', {
        'teams': page,
        'page': page,
        'competitions': competitions,
        'selected_competition': competition_id,
    })
