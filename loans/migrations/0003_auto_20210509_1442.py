# Generated by Django 3.2.2 on 2021-05-09 14:42

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loans', '0002_alter_loan_interest_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='edited_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='loan',
            name='requested_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='loan',
            name='beneficiary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beneficiary', to=settings.AUTH_USER_MODEL),
        ),
    ]
