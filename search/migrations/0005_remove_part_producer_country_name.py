# Generated by Django 5.1 on 2024-08-08 18:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("search", "0004_remove_part_search_part_name_5673ca_idx_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="part",
            name="producer_country_name",
        ),
    ]
