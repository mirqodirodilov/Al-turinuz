# Generated by Django 4.2 on 2023-04-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0022_remove_result_reception_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result_reception',
            name='text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
