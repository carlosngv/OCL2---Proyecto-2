# Generated by Django 4.0 on 2021-12-31 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_csv_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='reports'),
        ),
    ]
