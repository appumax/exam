# Generated by Django 5.0 on 2023-12-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_borrow_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='Return_date',
            field=models.DateField(null=True),
        ),
    ]
