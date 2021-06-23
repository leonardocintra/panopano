# Generated by Django 3.2.4 on 2021-06-20 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='gateway_pagamento',
            field=models.CharField(choices=[('mercado_pago', 'Mercado Pago'), ('pagseguro_uol', 'PagSeguro UOL')], default='mercado_pago', max_length=20),
        ),
    ]
