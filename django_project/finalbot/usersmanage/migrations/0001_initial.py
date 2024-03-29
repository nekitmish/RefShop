# Generated by Django 3.1.7 on 2021-03-19 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=20, verbose_name='Название товара')),
                ('thumb_url', models.CharField(max_length=200, verbose_name='Фото товара')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('quantity', models.IntegerField(verbose_name='Количество в наличии')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(verbose_name='ID покупателя')),
                ('item_id', models.IntegerField(verbose_name='ID товара')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('amount', models.IntegerField(verbose_name='Сумма покупки')),
                ('purchase_time', models.DateTimeField(auto_now_add=True, verbose_name='Время покупки')),
                ('buyer_name', models.CharField(max_length=50, verbose_name='Имя покупателя')),
                ('buyer_phone', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес доставки')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(unique=True, verbose_name='ID пользователя Телеграм')),
                ('name', models.CharField(max_length=50)),
                ('referral_id', models.BigIntegerField(verbose_name='ID пригласившего пользователя')),
                ('coins', models.IntegerField(verbose_name='Реферальные отчисления')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usersmanage.user', unique=True)),
                ('referrer_id', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Реферал',
                'verbose_name_plural': 'Рефералы',
            },
        ),
    ]
