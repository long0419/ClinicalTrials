# Generated by Django 2.0.1 on 2018-03-08 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicaltrials', '0019_remove_file_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicaltrial',
            name='adverseEvents',
            field=models.TextField(blank=True, null=True),
        ),
    ]
