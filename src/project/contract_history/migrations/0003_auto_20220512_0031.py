# Generated by Django 3.2.12 on 2022-05-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_history', '0002_scannerstate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scannerstate',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delete at'),
        ),
        migrations.AlterField(
            model_name='transferhistory',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delete at'),
        ),
    ]
