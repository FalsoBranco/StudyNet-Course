# Generated by Django 3.2.9 on 2021-12-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_comment_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
