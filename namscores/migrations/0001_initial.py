# Generated by Django 4.2.5 on 2023-10-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1name', models.CharField(max_length=200)),
                ('team1scores', models.IntegerField(max_length=240)),
                ('team2name', models.CharField(max_length=200)),
                ('team2scores', models.IntegerField(max_length=240)),
                ('league', models.CharField(max_length=200)),
            ],
        ),
    ]