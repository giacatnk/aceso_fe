# Generated by Django 4.2.10 on 2025-04-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes_predictor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='admission_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
