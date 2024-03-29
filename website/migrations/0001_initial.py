# Generated by Django 2.2.7 on 2019-11-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
                ('Email', models.EmailField(max_length=254)),
                ('cartao', models.IntegerField()),
                ('Pagamento', models.CharField(choices=[('AV', 'Parcelado em 2x'), ('P2', 'Parcelado em 2x'), ('P3', 'Parcelado em 3x')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, default=50, max_digits=1000)),
                ('disponivel', models.BooleanField(default=True)),
                ('quantidade', models.IntegerField(default=1)),
                ('tamanho', models.CharField(choices=[('pp', 'Extra pequeno')], max_length=2)),
            ],
        ),
    ]
