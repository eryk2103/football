from django.db import models
from django.db.models import ForeignKey


class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    country = ForeignKey('countries.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    stadium = ForeignKey('stadiums.Stadium', on_delete=models.SET_NULL, null=True, blank=True)
    logo_url = models.URLField(blank=True)
    is_national = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name