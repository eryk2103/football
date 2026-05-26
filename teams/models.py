from django.db import models
from django.db.models import ForeignKey
from django.utils.text import slugify


def team_logo_path(instance, filename):
    ext = filename.split('.')[-1]
    safe_name = slugify(instance.name)
    return f"team_logos/{safe_name}.{ext}"


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=20, unique=True)
    code = models.CharField(max_length=3, unique=True)
    country = ForeignKey('countries.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    stadium = ForeignKey('stadiums.Stadium', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.FileField(upload_to=team_logo_path, blank=True)
    is_national = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
