# Generated by Django 2.1.2 on 2018-10-29 05:23

from django.db import migrations, models
import shorturls.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly_name', models.CharField(error_messages={'unique': 'This friendly name is unavailabe.'}, help_text='Type in a friendly name you would like to use and we will check if it is available', max_length=128, validators=[shorturls.validators.FriendValidator])),
                ('short_url', models.CharField(max_length=128)),
                ('origin_domain', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('origin_ip', models.CharField(max_length=128)),
            ],
        ),
    ]
