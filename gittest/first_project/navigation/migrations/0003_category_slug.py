# Generated by Django 2.2.7 on 2020-06-02 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_auto_20200602_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
