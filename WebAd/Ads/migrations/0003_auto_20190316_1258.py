# Generated by Django 2.1 on 2019-03-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0002_adunit_imagead_textad'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagead',
            name='tags',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textad',
            name='tags',
            field=models.CharField(default='Null', max_length=1000),
            preserve_default=False,
        ),
    ]
