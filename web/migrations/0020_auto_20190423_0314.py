# Generated by Django 2.2 on 2019-04-23 10:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_auto_20190411_0050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='karkard',
            options={'verbose_name': 'ثبت کارکرد', 'verbose_name_plural': 'لیست کارکرد ها'},
        ),
        migrations.AlterField(
            model_name='sabteruz',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
