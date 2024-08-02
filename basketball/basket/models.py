from django.db import models

class league(models.Model):
    id = models.AutoField(primary_key=True)
    name_league = models.CharField(max_length=40)



class team(models.Model):
    id = models.AutoField(primary_key=True)
    name_team = models.CharField(max_length=30)
    id_league = models.ForeignKey(league, on_delete=models.CASCADE)



class player(models.Model):
    POSITIONS = [
        ('PG', 'Разыгрывающий защитник'),
        ('SG', 'Атакующий защитник'),
        ('SF', 'Легкий форвард'),
        ('PF', 'Мощный форвард'),
        ('C', 'Центровой'),
    ]

    HAND_CHOICES = [
        ('L', 'Левая'),
        ('R', 'Правая'),
        ('A', 'Амбидекстер'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    height_cm = models.IntegerField()
    weight_kg = models.IntegerField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITIONS)
    hand = models.CharField(max_length=1, choices=HAND_CHOICES)
    team_id = models.ForeignKey(team, on_delete=models.CASCADE)



class match(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    home_team = models.ForeignKey(team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(team, on_delete=models.CASCADE, related_name='away_matches')
    id_league = models.ForeignKey(league, on_delete=models.CASCADE)
    score_home = models.IntegerField()
    score_away = models.IntegerField()



class player_statistic(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(player, on_delete=models.CASCADE)
    match_id = models.ForeignKey(match, on_delete=models.CASCADE)
    points = models.IntegerField()
    rebounds = models.IntegerField()
    assists = models.IntegerField()
    blocks = models.IntegerField()
    steals = models.IntegerField()
    time = models.TimeField()



class team_statistic(models.Model):
    id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey(team, on_delete=models.CASCADE)
    match_id = models.ForeignKey(match, on_delete=models.CASCADE)
    points_scored = models.IntegerField()
    points_conceded = models.IntegerField()


