# Generated by Django 3.2.8 on 2022-06-13 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220612_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='estoque',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
    ]
