# Generated by Django 3.0.5 on 2021-10-12 08:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211010_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patien',
            name='PatNais',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]