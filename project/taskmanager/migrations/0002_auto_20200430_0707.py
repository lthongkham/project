# Generated by Django 2.1.15 on 2020-04-30 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='Name',
        ),
    ]