# Generated by Django 2.2 on 2020-05-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=30)),
                ('Paginas', models.IntegerField()),
                ('Editorial', models.CharField(max_length=40)),
            ],
        ),
    ]
