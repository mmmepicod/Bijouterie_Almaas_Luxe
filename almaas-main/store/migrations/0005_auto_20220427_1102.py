# Generated by Django 3.2.3 on 2022-04-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_auto_20210529_1741"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="en_promo",
            field=models.BooleanField(default=False, verbose_name="En promo"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="taux",
            field=models.DecimalField(
                blank=0, decimal_places=2, default=0, max_digits=4
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="address",
            name="city",
            field=models.CharField(max_length=150, verbose_name="Ville"),
        ),
        migrations.AlterField(
            model_name="address",
            name="locality",
            field=models.CharField(
                max_length=150,
                verbose_name="Région on met adresse? :models.py/adress pour modif)",
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="state",
            field=models.CharField(max_length=150, verbose_name="Pays"),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Accepted", "Accepted"),
                    ("Packed", "Packed"),
                    ("On The Way", "On The Way"),
                    ("Delivered", "Delivered"),
                    ("Cancelled", "Cancelled"),
                ],
                default="Pending",
                max_length=50,
            ),
        ),
    ]
