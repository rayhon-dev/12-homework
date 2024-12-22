# Generated by Django 5.1.4 on 2024-12-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]
