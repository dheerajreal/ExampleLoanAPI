# Generated by Django 3.2.2 on 2021-05-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0003_auto_20210509_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='edited_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='requested_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]