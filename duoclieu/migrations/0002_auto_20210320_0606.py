# Generated by Django 3.1.6 on 2021-03-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duoclieu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hothucvat',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True),
        ),
    ]
