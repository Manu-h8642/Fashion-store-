# Generated by Django 5.0 on 2024-01-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_wishlistdb_uname'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartdb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
