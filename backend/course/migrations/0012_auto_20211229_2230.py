# Generated by Django 3.2.9 on 2021-12-30 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['name', '-created_at'], 'verbose_name': 'comment', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['title', '-created_at'], 'verbose_name': 'course', 'verbose_name_plural': 'courses'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['title', '-created_at'], 'verbose_name': 'lesson', 'verbose_name_plural': 'lessons'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lesson',
        ),
        migrations.AddField(
            model_name='comment',
            name='Lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.lesson'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, help_text='format: required, letters, numbers, underscore, or hyphens', max_length=150, verbose_name='course safe URL'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.course'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='comment name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='course.Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='uploads/default.png', help_text='format: required, default-default.png', upload_to='uploads/', verbose_name='product image'),
        ),
        migrations.AlterField(
            model_name='course',
            name='long_description',
            field=models.TextField(blank=True, help_text='course long description', null=True, verbose_name='Long description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_description',
            field=models.TextField(blank=True, help_text='course shot description', null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='course title'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('A', 'article'), ('Q', 'quiz')], help_text='format: required, max-1', max_length=1, verbose_name='lesson type'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='long_description',
            field=models.TextField(blank=True, help_text='lesson long description', null=True, verbose_name='Long description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='short_description',
            field=models.TextField(blank=True, help_text='lesson shot description', null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('D', 'draft'), ('P', 'published')], help_text='format: required, max-1', max_length=1, verbose_name='lesson status'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(help_text='format: required, max-255', max_length=255, verbose_name='lesson title'),
        ),
    ]
