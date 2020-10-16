# Generated by Django 2.1.5 on 2020-10-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20201016_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='wishlist_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('T', 'Toys'), ('A', 'Accessories'), ('M', ''), ('H', 'Home Decor')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'Sale'), ('O', 'Out of Stock'), ('N', 'New')], max_length=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.Order_Item'),
        ),
    ]
