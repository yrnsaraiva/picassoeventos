# Generated by Django 5.0.1 on 2024-02-01 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_event_cover_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PastEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_image', models.ImageField(default='no-photo.svg', null=True, upload_to='')),
                ('date', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('gallery_link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
