# Generated by Django 3.2.5 on 2022-10-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20221002_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(related_name='subtasks', to='account.Subtask'),
        ),
    ]
