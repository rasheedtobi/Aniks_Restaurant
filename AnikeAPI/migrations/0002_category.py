# Generated by Django 4.2.1 on 2023-05-24 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnikeAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]