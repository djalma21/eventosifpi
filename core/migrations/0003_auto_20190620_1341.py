# Generated by Django 2.2.2 on 2019-06-20 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190619_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='nome',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
