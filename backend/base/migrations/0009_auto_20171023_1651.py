# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 13:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_auto_20171022_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameSurname', models.CharField(blank=True, max_length=500, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('moderatorDate', models.DateTimeField(blank=True, null=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='annotation',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audioanno',
            name='endTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='audioanno',
            name='startTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imageanno',
            name='pixelX',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imageanno',
            name='pixelY',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='featured_img',
            field=models.FileField(blank=True, null=True, upload_to='item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longtitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='textanno',
            name='endChar',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='textanno',
            name='startChar',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userratedannotation',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userratedcomment',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userrateditem',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videoanno',
            name='endTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videoanno',
            name='startTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]