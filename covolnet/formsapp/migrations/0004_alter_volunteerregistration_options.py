# Generated by Django 3.2 on 2021-04-26 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0003_alter_volunteerregistration_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteerregistration',
            options={'ordering': ['verified']},
        ),
    ]
