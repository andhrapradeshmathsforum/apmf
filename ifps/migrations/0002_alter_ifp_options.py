# Generated by Django 5.0.3 on 2024-04-21 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ifp',
            options={'ordering': ['date_added'], 'verbose_name': 'IFP Usage Video', 'verbose_name_plural': 'IFP Usage Videos'},
        ),
    ]