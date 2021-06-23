# Generated by Django 3.2.3 on 2021-06-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0014_produto_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, unique=True, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Variação',
                'verbose_name_plural': 'Variações',
                'db_table': 'variacao',
                'ordering': ('descricao',),
            },
        ),
    ]
