# Generated by Django 3.2.15 on 2022-09-19 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=12)),
                ('content', models.TextField(blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-create_at',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=5)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post')),
            ],
            options={
                'ordering': ('-create_at',),
            },
        ),
    ]
