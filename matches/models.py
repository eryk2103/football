from django.db import models

class Match(models.Model):
    class Status(models.TextChoices):
        PLAYING = 'PLAYING', 'Playing'
        HALF_TIME = 'HALF_TIME', 'Half Time'
        EXTRA_TIME = 'EXTRA_TIME', 'Extra Time'
        PENALTY_SHOOTOUT = 'PENALTY_SHOOTOUT', 'Penalty Shootout'
        FINISHED = 'FINISHED', 'Finished'
        POSTPONED = 'POSTPONED', 'Postponed'
        TBC = 'TBC', 'TBC'

    home_team = models.ForeignKey('teams.Team', related_name="home_matches", on_delete=models.SET_NULL, null=True, blank=True)
    away_team = models.ForeignKey('teams.Team', related_name="away_matches", on_delete=models.SET_NULL, null=True, blank=True)
    home_score = models.PositiveIntegerField(null=True, blank=True)
    away_score = models.PositiveIntegerField(null=True, blank=True)
    penalty_home_score = models.PositiveIntegerField(null=True, blank=True)
    penalty_away_score = models.PositiveIntegerField(null=True, blank=True)
    competition = models.ForeignKey('competitions.CompetitionPhase', on_delete=models.SET_NULL, null=True, blank=True)
    stadium = models.ForeignKey('stadiums.Stadium', on_delete=models.SET_NULL, null=True, blank=True)
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status)
    leg = models.PositiveSmallIntegerField(null=True, blank=True) # 1 or 2
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

