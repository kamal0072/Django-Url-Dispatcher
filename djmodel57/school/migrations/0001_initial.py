# Generated by Django 3.1.6 on 2021-03-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=90)),
                ('s_roll', models.IntegerField()),
                ('s_email', models.EmailField(max_length=90)),
            ],
        ),
    ]
