# Generated by Django 4.2.4 on 2023-08-31 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]