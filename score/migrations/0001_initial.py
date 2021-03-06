# Generated by Django 2.1 on 2019-01-12 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='before',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('pname', models.CharField(max_length=100)),
                ('placeS', models.IntegerField()),
                ('placeF', models.IntegerField()),
                ('skill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamename', models.CharField(max_length=100)),
                ('score', models.CharField(max_length=100)),
                ('keioS', models.CharField(max_length=100)),
                ('keioV', models.CharField(max_length=100)),
                ('eS', models.CharField(max_length=100)),
                ('eV', models.CharField(max_length=100)),
                ('eteam', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField()),
                ('pname', models.CharField(max_length=100)),
                ('placeS', models.IntegerField()),
                ('placeF', models.IntegerField()),
                ('skill', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
            ],
        ),
    ]
