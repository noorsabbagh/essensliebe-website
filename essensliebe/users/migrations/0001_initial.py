# Generated by Django 2.1 on 2018-08-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]