# Generated by Django 4.1.4 on 2023-01-22 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_inflight_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounce',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='base.startgame'),
        ),
    ]
