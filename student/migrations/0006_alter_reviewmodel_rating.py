# Generated by Django 4.2.4 on 2024-02-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_reviewmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='rating',
            field=models.IntegerField(),
        ),
    ]