# Generated by Django 4.1.4 on 2023-02-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(),
        ),
    ]
