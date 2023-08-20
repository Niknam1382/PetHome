# Generated by Django 4.2.3 on 2023-08-20 05:41

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0015_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[283, 202], upload_to='blog', verbose_name='عکس'),
        ),
    ]
