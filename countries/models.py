from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name