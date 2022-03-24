# Generated by Django 3.2.12 on 2022-02-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='blood',
            field=models.CharField(choices=[('zeos', 'Zeos'), ('poseidon', 'Poseidon'), ('hades', 'Hades'), ('hestia', 'Hestia'), ('hera', 'Hera'), ('aphrodite', 'Aphrodite'), ('atena', 'Atena'), ('ares', 'Ares'), ('hermes', 'Hermes')], max_length=32, verbose_name='Blood'),
        ),
        migrations.AlterField(
            model_name='nft',
            name='speciality',
            field=models.CharField(choices=[('enhancer', 'Enhancer'), ('double_counter', 'Double counter'), ('magnet', 'Magnet'), ('counter_breaker', 'Counter breaker'), ('special_drop', 'Special drop')], max_length=32, verbose_name='Speciality'),
        ),
    ]