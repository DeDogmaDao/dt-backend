# Generated by Django 3.2.12 on 2022-02-19 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('round', '0001_initial'),
        ('nft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulldeck',
            name='round',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='round.round', verbose_name='Round'),
        ),
        migrations.AddField(
            model_name='chosencard',
            name='deck_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nft.fulldeck', verbose_name='Deck place'),
        ),
    ]
