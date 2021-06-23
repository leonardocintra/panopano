# Generated by Django 3.2.4 on 2021-06-20 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_pedido_gateway_pagamento'),
        ('pagamento', '0003_pagamento_gateway_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamentomercadopago',
            name='pedido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_mercado_pago_pedido', to='pedido.pedido'),
        ),
        migrations.DeleteModel(
            name='Pagamento',
        ),
    ]
