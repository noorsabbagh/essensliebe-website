# Generated by Django 2.1 on 2018-08-22 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directmessage', '0004_auto_20180822_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directmessage',
            options={'ordering': ['-sent']},
        ),
    ]
