# Generated by Django 3.2 on 2023-02-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(blank=True, choices=[('color', 'color'), ('size', 'size')], max_length=100, null=True),
        ),
    ]
