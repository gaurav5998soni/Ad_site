# Generated by Django 2.1 on 2019-03-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0005_auto_20190317_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagead',
            name='horizontal_img',
            field=models.ImageField(upload_to='adImages'),
        ),
        migrations.AlterField(
            model_name='imagead',
            name='square_img',
            field=models.ImageField(upload_to='adImages'),
        ),
        migrations.AlterField(
            model_name='imagead',
            name='verticle_img',
            field=models.ImageField(upload_to='adImages'),
        ),
    ]