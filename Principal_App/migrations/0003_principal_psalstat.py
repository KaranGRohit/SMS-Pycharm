# Generated by Django 2.1.4 on 2019-02-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal_App', '0002_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='principal',
            name='PSalStat',
            field=models.BooleanField(default=False),
        ),
    ]