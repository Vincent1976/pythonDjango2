# Generated by Django 2.1.15 on 2022-03-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
