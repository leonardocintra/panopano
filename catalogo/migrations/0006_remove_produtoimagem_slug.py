# Generated by Django 3.2 on 2021-04-27 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_produtoimagem_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtoimagem',
            name='slug',
        ),
    ]
