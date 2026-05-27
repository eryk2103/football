from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Match
from competitions.models import Competition, CompetitionPhase


def index(request):
    competitions = Competition.objects.order_by('name')
    phases = CompetitionPhase.objects.none()

    competition_id = request.GET.get('competition')
    phase_id = request.GET.get('phase')
    order = request.GET.get('order', 'asc')

    date_order = 'datetime' if order == 'asc' else '-datetime'
    matches = Match.objects.select_related('home_team', 'away_team', 'competition', 'competition__competition',
                                           'stadium').order_by(date_order)

    if competition_id:
        matches = matches.filter(competition__competition_id=competition_id)
        phases = CompetitionPhase.objects.filter(competition_id=competition_id).order_by('name')

    if phase_id:
        matches = matches.filter(competition_id=phase_id)

    paginator = Paginator(matches, 25)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'matches/index.html', {
        'matches': page,
        'page': page,
        'competitions': competitions,
        'phases': phases,
        'selected_competition': competition_id,
        'selected_phase': phase_id,
        'order': order,
    })


def show(request, pk):
    match = get_object_or_404(
        Match.objects.select_related(
            'home_team', 'away_team',
            'competition', 'competition__competition',
            'stadium',
        ),
        pk=pk,
    )
    return render(request, 'matches/show.html', {'match': match})
