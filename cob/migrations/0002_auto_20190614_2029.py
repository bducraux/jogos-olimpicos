# Generated by Django 2.2.2 on 2019-06-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cob', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='nome',
            field=models.CharField(max_length=200, unique=True, verbose_name='Nome do atleta'),
        ),
    ]