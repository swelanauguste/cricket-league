# Generated by Django 4.0.4 on 2022-05-19 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BattingStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bat_style', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BowlingStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bowl_style', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100, unique=True)),
                ('player_dob', models.DateField()),
                ('bat_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.battingstyle')),
                ('bowl_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.bowlingstyle')),
                ('teams', models.ManyToManyField(blank=True, to='teams.team')),
            ],
        ),
    ]
