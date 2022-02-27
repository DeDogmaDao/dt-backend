# Generated by Django 3.2.12 on 2022-02-27 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0004_alter_chosencard_deck_place'),
        ('blockchain_transaction', '0001_initial'),
        ('round', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='round',
            old_name='winner_prize',
            new_name='winners_total_prize',
        ),
        migrations.RemoveField(
            model_name='round',
            name='winner_nft',
        ),
        migrations.RemoveField(
            model_name='round',
            name='winner_wallet',
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='Delete at')),
                ('winner_wallet', models.CharField(max_length=1024, verbose_name='Winner wallet')),
                ('fulfill_status', models.CharField(choices=[('fulfilled', 'Fulfilled'), ('unfulfilled', 'Unfulfilled'), ('partially_fulfilled', 'Partially fulfilled')], max_length=100)),
                ('is_original_winner', models.BooleanField(verbose_name='Is original winner')),
                ('winner_type', models.CharField(choices=[('common', 'Common'), ('god', 'God')], max_length=100, verbose_name='Winner type')),
                ('winner_portion', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Winner portion')),
                ('round', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='round_winners', to='round.round', verbose_name='Round')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winners', to='blockchain_transaction.transaction', verbose_name='Transaction')),
                ('winner_nft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nft.nft', verbose_name='Winner nft')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
