# Generated by Django 2.1 on 2019-05-07 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalyear', '0007_auto_20190507_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualpayment',
            name='farmer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]