# Generated by Django 3.2.12 on 2022-06-29 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0014_nft_is_revealed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fulldeck',
            name='wallet',
            field=models.CharField(max_length=1024, verbose_name='Wallet'),
        ),
    ]
