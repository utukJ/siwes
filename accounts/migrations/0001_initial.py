# Generated by Django 3.2.5 on 2021-08-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric', models.CharField(default='', max_length=9)),
                ('sws_start_date', models.DateField()),
            ],
        ),
    ]