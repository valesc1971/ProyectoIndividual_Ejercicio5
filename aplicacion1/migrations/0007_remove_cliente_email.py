# Generated by Django 4.0.4 on 2022-04-28 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0006_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
    ]
