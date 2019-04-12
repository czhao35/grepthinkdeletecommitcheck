# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.PositiveIntegerField()),
                ('interest_reason', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_reason', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Project Title Provided', max_length=255)),
                ('tagline', models.TextField(default='Default Project Tagline', max_length=38)),
                ('content', models.TextField(default='Content', max_length=4000)),
                ('ta_location', models.TextField(default='', max_length=38)),
                ('ta_time', models.TextField(default='', max_length=38)),
                ('avail_mem', models.BooleanField(default=True)),
                ('sponsor', models.BooleanField(default=False)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('project_image', models.TextField(default='http://i.imgur.com/5Z17VfH.png', max_length=100)),
                ('resource', models.TextField(default='*No resources provided*', max_length=4000)),
                ('teamSize', models.IntegerField(default=4)),
                ('meetings', models.TextField(default='')),
                ('readable_meetings', models.TextField(null=True)),
                ('weigh_interest', models.IntegerField(default=1)),
                ('weigh_know', models.IntegerField(default=1)),
                ('weigh_learn', models.IntegerField(default=1)),
                ('assigned_ta', models.ManyToManyField(default='', related_name='assigned_ta', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_creator', to=settings.AUTH_USER_MODEL)),
                ('desired_skills', models.ManyToManyField(default='', related_name='desired', to='profiles.Skills')),
                ('interest', models.ManyToManyField(default=None, related_name='project_interest', to='projects.Interest')),
                ('members', models.ManyToManyField(related_name='membership', through='projects.Membership', to=settings.AUTH_USER_MODEL)),
                ('pending_invitations', models.ManyToManyField(default='', related_name='invitations', to=settings.AUTH_USER_MODEL)),
                ('pending_members', models.ManyToManyField(default='', related_name='pending', to=settings.AUTH_USER_MODEL)),
                ('scrum_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrum_master', to=settings.AUTH_USER_MODEL)),
                ('ta', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='ta', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(default='', max_length=2000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_chat', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='projects.Project')),
            ],
            options={
                'verbose_name': 'Project Chat',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_title', models.CharField(default='Default Update Title', max_length=255)),
                ('update', models.TextField(default='Default Update', max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project Update',
                'verbose_name_plural': 'Project Updates',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='ResourceUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('src_title', models.CharField(default='Default Resource Title', max_length=255)),
                ('src_link', models.URLField(default='Default Resource Link', max_length=2000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resource Update',
                'verbose_name_plural': 'Resource Updates',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Tsr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_number', models.DecimalField(decimal_places=0, default=1, max_digits=2)),
                ('percent_contribution', models.DecimalField(decimal_places=0, max_digits=2)),
                ('positive_feedback', models.CharField(default='', max_length=255)),
                ('negative_feedback', models.CharField(default='', max_length=255)),
                ('tasks_completed', models.CharField(default='', max_length=255)),
                ('performance_assessment', models.CharField(default='', max_length=255)),
                ('notes', models.CharField(default='', max_length=255)),
                ('evaluatee', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='evaluatee', to=settings.AUTH_USER_MODEL)),
                ('evaluator', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='evaluator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tsr',
            field=models.ManyToManyField(default=None, related_name='project_tsr', to='projects.Tsr'),
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='membershipUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
