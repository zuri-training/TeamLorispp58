# Generated by Django 4.1.4 on 2022-12-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debtor',
            name='academic_session',
            field=models.DateField(),
        ),
    ]