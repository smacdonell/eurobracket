# Generated by Django 3.2.1 on 2021-06-23 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210623_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='prev_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.game'),
        ),
    ]
