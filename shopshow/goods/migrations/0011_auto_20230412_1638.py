# Generated by Django 3.1.3 on 2023-04-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20230311_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allgoods',
            name='Product_img',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
