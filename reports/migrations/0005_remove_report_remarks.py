# Generated by Django 4.0 on 2021-12-31 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_report_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='remarks',
        ),
    ]
