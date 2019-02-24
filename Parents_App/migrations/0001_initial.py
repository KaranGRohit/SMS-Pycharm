# Generated by Django 2.1.4 on 2019-02-05 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Student_App', '0006_student_sgender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrFname', models.CharField(max_length=20)),
                ('PrLname', models.CharField(max_length=20)),
                ('PrContactNo', models.IntegerField()),
                ('PrSId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Student_App.Student')),
            ],
        ),
    ]