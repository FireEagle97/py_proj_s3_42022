# Generated by Django 4.0.4 on 2022-05-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemCatalog', '0006_remove_item_likes_item_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_flagged',
            field=models.BooleanField(default=False),
        ),
    ]