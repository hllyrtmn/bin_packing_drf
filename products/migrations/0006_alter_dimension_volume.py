# Generated by Django 5.1.3 on 2024-12-02 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_dimension_depth_alter_dimension_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimension',
            name='volume',
            field=models.DecimalField(decimal_places=10, editable=False, max_digits=20),
        ),
    ]