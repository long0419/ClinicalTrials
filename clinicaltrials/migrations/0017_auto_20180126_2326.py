# Generated by Django 2.0.1 on 2018-01-26 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaltrials', '0016_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]