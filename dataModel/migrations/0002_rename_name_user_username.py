# Generated by Django 4.0.3 on 2022-03-28 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]