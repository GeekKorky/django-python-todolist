# Generated by Django 2.0.1 on 2018-12-11 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181211_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='username',
            new_name='user',
        ),
    ]
