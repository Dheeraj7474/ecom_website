# Generated by Django 4.2 on 2023-04-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cogs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='dep',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='interest_exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='op_exp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='revenue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='taxes',
            field=models.IntegerField(default=0),
        ),
    ]
