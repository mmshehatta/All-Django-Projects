# Generated by Django 3.2.3 on 2021-05-26 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='bio', max_length=150),
        ),
    ]
