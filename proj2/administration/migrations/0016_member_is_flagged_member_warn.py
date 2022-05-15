# Generated by Django 4.0.4 on 2022-05-15 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_member_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_flagged',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Member_Warn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_warned', models.BooleanField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='administration.member')),
            ],
        ),
    ]