from django.db import models
from django.db.models import ForeignKey


class Competition(models.Model):
    class Format(models.TextChoices):
        LEAGUE = 'LEAGUE', 'League'
        CUP = 'CUP', 'Cup'
        LEAGUE_KNOCKOUT = 'LEAGUE_KNOCKOUT', 'League Knockout'

    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20, blank=True)
    format = models.CharField(max_length=20, choices=Format)
    country = ForeignKey('countries.Country', on_delete=models.SET_NULL, null=True, blank=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    logo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + str(self.start_year) + '/' + str(self.end_year)


class CompetitionPhase(models.Model):
    class Type(models.TextChoices):
        GROUP_STAGE = 'GROUP_STAGE', 'Group Stage'
        KNOCKOUT_STAGE = 'KNOCKOUT_STAGE', 'Knockout Stage'
        LEAGUE_STAGE = 'LEAGUE_STAGE', 'League Stage'

    competition = models.ForeignKey('competitions.Competition', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=Type)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.competition} - {self.type} - {self.name}"
