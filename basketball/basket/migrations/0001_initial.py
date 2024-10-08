# Generated by Django 5.0.7 on 2024-08-02 00:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leagues',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_league', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('height_cm', models.IntegerField()),
                ('weight_kg', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
                ('login', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('PG', 'Разыгрывающий защитник'), ('SG', 'Атакующий защитник'), ('SF', 'Легкий форвард'), ('PF', 'Силовой форвард'), ('C', 'Центровой')], max_length=2)),
                ('hand', models.CharField(choices=[('L', 'Левая'), ('R', 'Правая'), ('A', 'Амбидекстер')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='matches',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('score_home', models.IntegerField()),
                ('score_away', models.IntegerField()),
                ('id_league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.leagues')),
            ],
        ),
        migrations.CreateModel(
            name='player_stats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('rebounds', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('blocks', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('time', models.TimeField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.matches')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.players')),
            ],
        ),
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_team', models.CharField(max_length=30)),
                ('id_league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.leagues')),
            ],
        ),
        migrations.CreateModel(
            name='team_stats',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('points_scored', models.IntegerField()),
                ('points_conceded', models.IntegerField()),
                ('match_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.matches')),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.teams')),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='basket.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='basket.teams'),
        ),
    ]
