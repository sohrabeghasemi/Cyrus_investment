# Generated by Django 2.2 on 2019-04-22 16:30

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_auto_20190422_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sabteruz',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
