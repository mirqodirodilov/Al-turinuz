# Generated by Django 4.2 on 2023-04-28 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_aboutpagemodel_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indexfirstmodel',
            name='description',
        ),
    ]