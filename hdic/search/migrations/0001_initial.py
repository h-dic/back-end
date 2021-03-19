# Generated by Django 3.0.4 on 2020-03-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_plante', models.CharField(max_length=200)),
                ('effets_plante', models.CharField(max_length=200)),
                ('intensite_plante', models.CharField(max_length=200)),
                ('nom_med', models.CharField(max_length=200)),
                ('effets_med', models.CharField(max_length=200)),
                ('intensite_med', models.CharField(max_length=200)),
                ('consequence', models.CharField(max_length=200)),
            ],
        ),
    ]