# Generated by Django 2.2 on 2020-05-14 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0002_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='biblio.Autor'),
        ),
    ]
