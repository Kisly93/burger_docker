# Generated by Django 3.2.15 on 2023-09-30 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0042_auto_20230930_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.PositiveIntegerField(choices=[(1, 'Наличные'), (2, 'Электронно')], db_index=True, default=1, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='called_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Время звонка менеджера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='registered_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Время регистрации'),
        ),
    ]
