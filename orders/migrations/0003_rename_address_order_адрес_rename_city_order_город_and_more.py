# Generated by Django 4.1.2 on 2022-10-24 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_first_name_order_имя'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='Адрес',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='Город',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='postal_code',
            new_name='Индекс',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='Почта',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='Фамилия',
        ),
    ]
