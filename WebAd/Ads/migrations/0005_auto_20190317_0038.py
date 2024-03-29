# Generated by Django 2.1 on 2019-03-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0004_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='imageAd',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imageAd', to='Ads.ImageAd'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='textAd',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='textAd', to='Ads.TextAd'),
        ),
    ]
