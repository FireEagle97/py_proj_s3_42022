# Generated by Django 4.0.3 on 2022-05-17 01:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=800)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('address', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('New', 'New'), ('Like New', 'Like New'), ('Used', 'Used')], default='New', max_length=10)),
                ('image', models.ImageField(default='item_default_image.jpg', upload_to='item_pics/')),
                ('is_liked', models.BooleanField(default=False)),
                ('is_flagged', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.member')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('comment', models.TextField(default='', max_length=250)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.member')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itemCatalog.item')),
            ],
        ),
    ]
