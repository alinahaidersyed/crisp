# Generated by Django 5.0.4 on 2024-04-17 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_record_city_remove_record_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('voucher_number', models.CharField(max_length=10)),
                ('is_free_umbrella', models.BooleanField(default=False)),
            ],
        ),
    ]
