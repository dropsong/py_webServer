# Generated by Django 4.2 on 2024-10-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0007_areas'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='booktest')),
            ],
        ),
    ]
