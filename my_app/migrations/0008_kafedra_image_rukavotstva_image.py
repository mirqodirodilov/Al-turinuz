# Generated by Django 4.2 on 2023-04-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_kafedra_rukavotstva'),
    ]

    operations = [
        migrations.AddField(
            model_name='kafedra',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rukavotstva',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]