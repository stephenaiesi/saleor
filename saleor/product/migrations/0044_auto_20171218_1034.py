# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django_prices.models


def split_product_price_to_price_net_and_gross(apps, schema_editor):
    Product = apps.get_model('product', 'Product')
    for product in Product.objects.all():
        product.price_net = product.price
        product.price_gross = product.price
        product.save()


def split_product_variant_price_to_price_net_and_gross(apps, schema_editor):
    ProductVariant = apps.get_model('product', 'ProductVariant')
    for product_variant in ProductVariant.objects.all():
        product_variant.price_net = product_variant.price
        product_variant.price_gross = product_variant.price
        product_variant.save()


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0043_auto_20171207_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=django_prices.models.AmountField(verbose_name='price', max_digits=12, decimal_places=2, currency='USD', blank=True, null=True)),
        migrations.AddField(
            model_name='product',
            name='price_net',
            field=django_prices.models.AmountField(verbose_name='price net', max_digits=12, decimal_places=2, currency='USD', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price_gross',
            field=django_prices.models.AmountField(verbose_name='price gross', max_digits=12, decimal_places=2, currency='USD', blank=True, null=True),
        ),
        migrations.RunPython(split_product_price_to_price_net_and_gross),
        migrations.AlterField(
            model_name='productvariant',
            name='price_override',
            field=django_prices.models.AmountField(verbose_name='price_override',
                                                   max_digits=12,
                                                   decimal_places=2,
                                                   currency='USD', blank=True,
                                                   null=True)),
        migrations.AddField(
            model_name='productvariant',
            name='price_override_net',
            field=django_prices.models.AmountField(verbose_name='price override net',
                                                   max_digits=12,
                                                   decimal_places=2,
                                                   currency='USD', blank=True,
                                                   null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='price_override_gross',
            field=django_prices.models.AmountField(verbose_name='price override gross',
                                                   max_digits=12,
                                                   decimal_places=2,
                                                   currency='USD', blank=True,
                                                   null=True),
        ),
    ]
