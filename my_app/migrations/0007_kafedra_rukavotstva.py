# Generated by Django 4.2 on 2023-04-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_indexnewspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavozm', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Руководители кафедра',
                'verbose_name_plural': 'Руководители кафедра',
            },
        ),
        migrations.CreateModel(
            name='Rukavotstva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lavozm', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Руководство',
                'verbose_name_plural': 'Руководство',
            },
        ),
    ]
