# Generated by Django 4.0.4 on 2022-05-22 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tasklabelrelation_task_labels_alter_task_executive_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='labels',
            new_name='label',
        ),
    ]
