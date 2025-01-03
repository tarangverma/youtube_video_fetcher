# Generated by Django 5.1.4 on 2024-12-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('thumbnails', models.JSONField()),
                ('video_id', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-published_at'],
                'indexes': [models.Index(fields=['published_at'], name='videos_vide_publish_dd5f2e_idx')],
            },
        ),
    ]
