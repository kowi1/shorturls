# Generated by Django 2.1.2 on 2018-11-21 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorturls', '0003_auto_20181030_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlentry',
            old_name='friendly_key',
            new_name='FriendlyKey',
        ),
        migrations.RenameField(
            model_name='urlentry',
            old_name='friendly_name',
            new_name='FriendlyName',
        ),
        migrations.RenameField(
            model_name='urlentry',
            old_name='origin_domain',
            new_name='OriginDomain',
        ),
        migrations.RenameField(
            model_name='urlentry',
            old_name='origin_ip',
            new_name='OriginIp',
        ),
        migrations.RenameField(
            model_name='urlentry',
            old_name='short_url',
            new_name='ShortUrl',
        ),
        migrations.RenameField(
            model_name='urlentry',
            old_name='views',
            new_name='Views',
        ),
    ]