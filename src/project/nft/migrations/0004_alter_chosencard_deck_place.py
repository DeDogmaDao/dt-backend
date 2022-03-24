# Generated by Django 3.2.12 on 2022-02-27 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0003_auto_20220220_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chosencard',
            name='deck_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chosen_cards', to='nft.fulldeck', verbose_name='Deck place'),
        ),
    ]