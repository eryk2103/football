from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Standing
from competitions.models import Competition, CompetitionPhase
from matches.models import Match


def index(request):
    competitions = Competition.objects.order_by('name')
    standings = Standing.objects.none()
    knockout_phases = []
    competition = None

    competition_id = request.GET.get('competition')

    if competition_id:
        competition = get_object_or_404(Competition, pk=competition_id)

        standings = (
            Standing.objects
            .filter(competition_id=competition_id)
            .select_related('team')
            .order_by('position')
        )

        if competition.format == Competition.Format.LEAGUE_KNOCKOUT:
            knockout_matches_qs = Match.objects.select_related(
                'home_team', 'away_team'
            ).order_by('datetime')

            knockout_phases = (
                CompetitionPhase.objects
                .filter(
                    competition_id=competition_id,
                    type=CompetitionPhase.Type.KNOCKOUT_STAGE,
                )
                .prefetch_related(Prefetch('match_set', queryset=knockout_matches_qs))
                .order_by('order')
            )

    return render(request, 'standings/index.html', {
        'competitions': competitions,
        'competition': competition,
        'standings': standings,
        'knockout_phases': knockout_phases,
        'selected_competition': competition_id,
    })
