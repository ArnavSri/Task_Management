# Generated by Django 5.1.6 on 2025-03-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='task_name',
        ),
        migrations.AlterField(
            model_name='task',
            name='completed_at',
            field=models.CharField(default='Work in progress', max_length=50),
        ),
    ]
