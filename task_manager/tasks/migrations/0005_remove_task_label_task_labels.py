# Generated by Django 4.0.4 on 2022-05-29 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0004_rename_labels_task_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='Labels', through='tasks.TaskLabelRelation', to='labels.label'),
        ),
    ]
