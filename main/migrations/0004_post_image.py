# Generated by Django 4.0 on 2022-03-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
