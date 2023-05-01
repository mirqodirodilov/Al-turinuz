# Generated by Django 4.2 on 2023-04-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_remove_indexfirstmodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexMiddlePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=25)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateField(auto_now=True)),
                ('views', models.CharField(max_length=25)),
            ],
        ),
    ]