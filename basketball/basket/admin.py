from django.contrib import admin
from .models import league, team, player, match, player_statistic, team_statistic

admin.site.register(league)
admin.site.register(team)
admin.site.register(player)
admin.site.register(match)
admin.site.register(player_statistic)
admin.site.register(team_statistic)

# Register your models here.
