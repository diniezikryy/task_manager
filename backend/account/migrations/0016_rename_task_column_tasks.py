# Generated by Django 3.2.5 on 2022-10-02 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20221002_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='task',
            new_name='tasks',
        ),
    ]