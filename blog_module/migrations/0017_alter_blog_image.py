# Generated by Django 4.2.3 on 2023-08-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0016_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='blog', verbose_name='عکس'),
        ),
    ]
