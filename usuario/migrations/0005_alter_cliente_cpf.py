# Generated by Django 3.2.4 on 2021-06-20 01:45

from django.db import migrations
import localflavor.br.models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_alter_cliente_peoplesoft_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=localflavor.br.models.BRCPFField(max_length=14, verbose_name='CPF'),
        ),
    ]
