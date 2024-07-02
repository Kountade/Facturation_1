# Generated by Django 4.2.4 on 2023-10-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("boutique", "0004_delete_blog"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="invoice",
            options={"verbose_name": "Invoice", "verbose_name_plural": "Invoices"},
        ),
        migrations.RenameField(
            model_name="invoice",
            old_name="last_update_date",
            new_name="last_updated_date",
        ),
        migrations.AlterField(
            model_name="article",
            name="name",
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name="article",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
        migrations.AlterField(
            model_name="article",
            name="unit_price",
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
        migrations.AlterField(
            model_name="customer",
            name="address",
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name="customer",
            name="city",
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=132),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(max_length=132),
        ),
        migrations.AlterField(
            model_name="customer",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Feminine")], max_length=1
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="zip_code",
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="comments",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="invoice_type",
            field=models.CharField(
                choices=[("R", "RECEIPT"), ("P", "PROFORMA INVOICE"), ("I", "INVOICE")],
                max_length=1,
            ),
        ),
    ]
