# Generated by Django 3.0.3 on 2020-02-10 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200210_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(default=10, max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default=10, max_length=200)),
                ('email', models.EmailField(default='test@test.tw', max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='character',
            old_name='account',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='character',
            name='password',
        ),
    ]
