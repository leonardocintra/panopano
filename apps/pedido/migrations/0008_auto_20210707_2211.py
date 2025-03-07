# Generated by Django 3.2.4 on 2021-07-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0007_pedido_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='valor_frete',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='pedido',
            name='valor_items',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
