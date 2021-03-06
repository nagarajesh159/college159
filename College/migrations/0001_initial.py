# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-04 07:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'others')], max_length=5)),
                ('department', models.CharField(choices=[('mech', 'mechanical engineering'), ('cse', 'computers science engineering'), ('eee', 'electrical engineering'), ('ece', 'electronic engineering')], max_length=5)),
                ('ssc_marklist', models.FileField(upload_to='document/')),
                ('inter_marklist', models.FileField(upload_to='document/')),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='image/')),
                ('department', models.CharField(choices=[('mech', 'mechanical engineering'), ('cse', 'computers science engineering'), ('eee', 'electrical engineering'), ('ece', 'electronic engineering')], max_length=5)),
                ('age', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'others')], max_length=5)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='College.Application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='image/')),
                ('age', models.IntegerField(default=0)),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='College.Application')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
