# Generated by Django 3.0.5 on 2021-10-17 09:07

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211012_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.BigAutoField(primary_key=True, serialize=False)),
                ('UserNom', models.TextField()),
                ('UserPass', models.CharField(default='', max_length=20)),
                ('is_active', models.IntegerField(null=True)),
            ],
            managers=[
                ('con_objet', django.db.models.manager.Manager()),
            ],
        ),
    ]
