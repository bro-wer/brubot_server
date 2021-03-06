# Generated by Django 2.1.2 on 2018-10-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0004_task_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerName', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('CC', 'Cannot connect'), ('WO', 'Working'), ('ID', 'Idle')], default='Cannot connect', max_length=5)),
            ],
        ),
    ]
