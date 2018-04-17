# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pod.authentication.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthenticationImageModel',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('image', models.ImageField(
                    blank=True,
                    max_length=255,
                    null=True,
                    upload_to=pod.authentication.models.get_upload_path_files,
                    verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('auth_type', models.CharField(
                    choices=[('local', 'local'), ('CAS', 'CAS')],
                    default='local',
                    max_length=20)),
                ('affiliation', models.CharField(
                    choices=[
                        ('member', 'member'), ('student', 'student')],
                    default='member', max_length=50)),
                ('commentaire', models.TextField(
                    blank=True, default='', verbose_name='Comment')),
                ('hashkey', models.CharField(
                    blank=True, default='', max_length=64, unique=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
                ('userpicture', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='authentication.AuthenticationImageModel',
                    verbose_name='Picture')),
            ],
        ),
    ]
