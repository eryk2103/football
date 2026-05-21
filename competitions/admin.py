from django.contrib import admin

from competitions.models import Competition, CompetitionPhase

admin.site.register(CompetitionPhase)
@admin.register(Competition)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "start_year", "end_year")
    search_fields = ("name",)