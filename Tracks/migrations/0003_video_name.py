# Generated by Django 5.0 on 2023-12-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0002_alter_artist_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]