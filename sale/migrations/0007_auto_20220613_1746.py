# Generated by Django 3.2.8 on 2022-06-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_alter_sale_total_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.AddField(
            model_name='sale',
            name='product_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
