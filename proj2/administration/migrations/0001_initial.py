# Generated by Django 4.0.4 on 2022-05-16 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_flagged', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='user_default_image.png', upload_to='user_pics')),
                ('group', models.ForeignKey(choices=[(1, 'Members'), (2, 'User Admin'), (3, 'Item Admin'), (4, 'Super User')], on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
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
