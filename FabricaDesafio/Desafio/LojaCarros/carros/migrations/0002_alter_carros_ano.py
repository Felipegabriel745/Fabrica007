# Generated by Django 4.1.7 on 2023-04-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='ano',
            field=models.IntegerField(),
        ),
    ]