# Generated by Django 3.2.5 on 2022-10-02 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20221002_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='tasks',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='account.task'),
        ),
    ]
