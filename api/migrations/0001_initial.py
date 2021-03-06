# Generated by Django 2.2 on 2019-05-16 02:50

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Skrypt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=12)),
                ('data', models.CharField(max_length=30)),
            ],
        ),
    ]
