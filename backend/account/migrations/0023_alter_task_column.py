# Generated by Django 3.2.5 on 2022-10-08 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_remove_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='account.column'),
        ),
    ]