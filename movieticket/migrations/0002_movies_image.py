# Generated by Django 2.0.2 on 2018-02-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='Usijali', upload_to=''),
            preserve_default=False,
        ),
    ]