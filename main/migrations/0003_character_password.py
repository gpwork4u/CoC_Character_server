# Generated by Django 3.0.3 on 2020-02-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_character_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='password',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
