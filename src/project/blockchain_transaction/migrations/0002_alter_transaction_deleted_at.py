# Generated by Django 3.2.12 on 2022-05-12 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain_transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delete at'),
        ),
    ]
