# Generated by Django 3.2.23 on 2024-02-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_actionrecord_exprecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionrecord',
            name='bvid',
            field=models.CharField(max_length=64, verbose_name='视频bvid'),
        ),
    ]
