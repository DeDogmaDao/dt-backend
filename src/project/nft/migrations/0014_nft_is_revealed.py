# Generated by Django 3.2.12 on 2022-05-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0013_auto_20220515_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='is_revealed',
            field=models.BooleanField(default=False, verbose_name='Is revealed'),
        ),
    ]