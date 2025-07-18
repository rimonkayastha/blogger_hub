# Generated by Django 5.2.3 on 2025-07-15 05:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_liked', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=2000)),
                ('published_date', models.DateField(default=None)),
                ('edited_date', models.DateField(blank=True, default=None, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts_written', to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(through='home.Like', through_fields=('post', 'user'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('published_date', models.DateField(default=None)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments_written', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
    ]
