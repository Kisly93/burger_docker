# Generated by Django 3.2.15 on 2023-10-05 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0047_order_chosen_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.AlterField(
            model_name='order',
            name='chosen_restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='foodcartapp.restaurant', verbose_name='Ресторан'),
        ),
    ]
