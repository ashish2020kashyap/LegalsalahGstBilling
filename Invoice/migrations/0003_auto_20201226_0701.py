# Generated by Django 3.1.4 on 2020-12-26 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0002_auto_20201226_0658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='category',
        ),
    ]
