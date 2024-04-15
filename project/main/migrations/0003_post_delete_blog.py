# Generated by Django 5.0.3 on 2024-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]