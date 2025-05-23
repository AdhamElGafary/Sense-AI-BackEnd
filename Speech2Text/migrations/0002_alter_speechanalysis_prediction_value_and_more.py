# Generated by Django 5.2 on 2025-04-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Speech2Text', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechanalysis',
            name='prediction_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='speechanalysis',
            name='sentiment',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='speechanalysis',
            name='transcription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
