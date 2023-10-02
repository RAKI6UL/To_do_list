# Generated by Django 4.2.3 on 2023-10-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=80)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
