# Generated by Django 4.2.1 on 2023-05-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=50)),
                ('preco', models.IntegerField()),
                ('img', models.TextField(max_length=99999)),
            ],
        ),
    ]