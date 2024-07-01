# Generated by Django 5.0.6 on 2024-07-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlChecker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('status_code', models.IntegerField(blank=True, null=True)),
                ('date_time_check', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
