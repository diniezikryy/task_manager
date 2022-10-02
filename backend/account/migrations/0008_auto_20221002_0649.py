# Generated by Django 3.2.5 on 2022-10-02 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_task_subtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='account.subtask'),
        ),
    ]
