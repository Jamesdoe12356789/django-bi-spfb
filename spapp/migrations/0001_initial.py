# Generated by Django 4.1.7 on 2023-03-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.TextField()),
                ('pwd', models.TextField(max_length=500)),
                ('Confirmpwd', models.TextField(max_length=500)),
                ('message', models.TextField(max_length=15000)),
            ],
        ),
    ]
