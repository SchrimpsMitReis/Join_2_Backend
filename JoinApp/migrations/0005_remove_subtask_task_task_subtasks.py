# Generated by Django 5.1.2 on 2025-02-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JoinApp', '0004_remove_task_subtasks_subtask_task_alter_task_prio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(related_name='tasks', to='JoinApp.subtask'),
        ),
    ]
