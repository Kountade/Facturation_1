# Generated by Django 4.2.2 on 2023-06-26 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("boutique", "0003_blog_alter_article_id_alter_customer_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="blog",
        ),
    ]
