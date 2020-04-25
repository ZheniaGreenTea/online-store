# Generated by Django 2.2.1 on 2020-04-20 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=250, verbose_name='страна')),
                ('street', models.CharField(max_length=250, verbose_name='улица')),
                ('house', models.CharField(max_length=250, verbose_name='дом')),
                ('apartment', models.CharField(max_length=250, verbose_name='квартира')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата загрузки ')),
                ('upload_date', models.DateTimeField(auto_now=True, verbose_name='дата обновления ')),
                ('is_active', models.BooleanField(verbose_name='адресс актуален?')),
            ],
            options={
                'verbose_name': 'Адресс',
                'verbose_name_plural': 'Адресса',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=250, verbose_name='страна')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата загрузки ')),
                ('upload_date', models.DateTimeField(auto_now=True, verbose_name='дата обновления ')),
                ('is_active', models.BooleanField(verbose_name='номер активен?')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250, verbose_name='имя')),
                ('lastname', models.CharField(max_length=250, verbose_name='фамилия')),
                ('adddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиль',
            },
        ),
    ]
