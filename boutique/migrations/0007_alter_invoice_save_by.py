# Generated by Django 4.2.4 on 2024-07-01 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("boutique", "0006_alter_invoice_save_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="save_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
