# Generated by Django 4.0.4 on 2022-05-19 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('matches', '0003_remove_match_player2_remove_match_player3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchplayer',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.team'),
        ),
    ]
