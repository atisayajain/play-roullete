# Generated by Django 3.2.9 on 2021-11-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_rename_bet_amount_bet_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game'),
        ),
    ]