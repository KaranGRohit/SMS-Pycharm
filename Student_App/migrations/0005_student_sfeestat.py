# Generated by Django 2.1.4 on 2019-02-05 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_App', '0004_auto_20190118_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SFeeStat',
            field=models.BooleanField(default=False),
        ),
    ]
