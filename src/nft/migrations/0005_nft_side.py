# Generated by Django 3.2.12 on 2022-03-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0004_alter_chosencard_deck_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='side',
            field=models.CharField(choices=[('will', 'Will'), ('talent', 'Talent')], max_length=100, null=True, verbose_name='Side'),
        ),
    ]
