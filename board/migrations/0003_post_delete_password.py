# Generated by Django 5.1.7 on 2025-04-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='delete_password',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
