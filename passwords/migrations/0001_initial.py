# Generated by Django 4.1.2 on 2022-10-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('user_or_email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('additional_notes', models.TextField(blank=True)),
                ('type_of_password', models.CharField(max_length=100)),
            ],
        ),
    ]
