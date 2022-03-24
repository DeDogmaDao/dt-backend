# Generated by Django 3.2.12 on 2022-02-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card_feature', '0001_initial'),
        ('nft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardpoint',
            name='nft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nft.nft', verbose_name='NFT'),
        ),
    ]