# Generated by Django 5.0.3 on 2024-04-21 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='key',
            options={'ordering': ['-standard', 'exam', 'year'], 'verbose_name': 'Principles of Valuation', 'verbose_name_plural': 'Principles of Valuation'},
        ),
    ]
