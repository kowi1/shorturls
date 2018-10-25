# Generated by Django 2.1.2 on 2018-10-25 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uniqueUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UrlEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendly_name', models.CharField(max_length=128)),
                ('short_url', models.URLField()),
                ('origin_domain', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('origin_ip', models.IntegerField(default=0)),
                ('origin_url', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shorturls.uniqueUrl')),
            ],
        ),
    ]
