# Generated by Django 4.2 on 2023-04-28 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0014_yangliklarmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Расписание занятий',
                'verbose_name_plural': 'Расписание занятий',
            },
        ),
    ]
