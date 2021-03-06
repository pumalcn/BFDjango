# Generated by Django 3.0.5 on 2020-04-19 19:41

import datetime
from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_of', models.PositiveSmallIntegerField(choices=[(1, 'DONE'), (2, 'IN_PROCESS'), (3, 'FROZEN')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'DONE'), (2, 'IN_PROCESS'), (3, 'FROZEN')], default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('priority', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskCommentManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=utils.upload.task_document_path, validators=[utils.validators.task_document_size, utils.validators.task_document_extension])),
            ],
        ),
        migrations.CreateModel(
            name='TaskManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
