# Generated by Django 4.0.4 on 2022-05-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_warned',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Member_Warn',
        ),
    ]
