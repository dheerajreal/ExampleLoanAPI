# Generated by Django 3.2.2 on 2021-05-09 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteuser',
            options={'ordering': ['pk']},
        ),
    ]
