# Generated by Django 4.2.5 on 2024-01-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtable',
            name='blgcmt',
            field=models.TextField(null=True),
        ),
    ]