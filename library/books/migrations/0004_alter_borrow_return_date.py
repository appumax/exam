# Generated by Django 5.0 on 2023-12-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_name_borrow_membership_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='Return_date',
            field=models.DateField(),
        ),
    ]
