# Generated by Django 2.2 on 2020-05-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0006_ejemplar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
                ('Telefono', models.BigIntegerField()),
                ('Direccion', models.CharField(max_length=40)),
            ],
        ),
    ]
