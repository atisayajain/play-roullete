# Generated by Django 3.2.9 on 2021-11-09 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casinos', '0002_rename_wallet_casino_account'),
        ('players', '0002_rename_wallet_player_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='casino',
        ),
        migrations.CreateModel(
            name='PlayerCasinoMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('casino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casinos.casino')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
            ],
        ),
    ]