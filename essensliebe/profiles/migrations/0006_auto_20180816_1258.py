# Generated by Django 2.1 on 2018-08-16 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_auto_20180816_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPrefrences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_food', models.CharField(blank=True, max_length=255, null=True)),
                ('vegan', models.BooleanField(blank=True, null=True)),
                ('vegetarian', models.BooleanField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerPrefrences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='prefrences',
            name='user',
        ),
        migrations.DeleteModel(
            name='Prefrences',
        ),
    ]
