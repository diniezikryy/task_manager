# Generated by Django 3.2.5 on 2022-10-08 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_task_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='column',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='account.column'),
        ),
    ]
