# Generated by Django 3.2.12 on 2022-05-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract_history', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannerState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete at')),
                ('last_scanned_block', models.PositiveBigIntegerField(verbose_name='Last scanned block')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
