# Generated by Django 4.2.1 on 2023-06-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_produtos_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoCarrinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('preco', models.IntegerField()),
                ('img', models.TextField(max_length=99999)),
            ],
        ),
    ]
