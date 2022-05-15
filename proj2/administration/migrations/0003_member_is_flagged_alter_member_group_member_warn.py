
# Generated by Django 4.0.4 on 2022-05-15 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('administration', '0002_remove_member_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_flagged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
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
