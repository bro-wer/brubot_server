# Generated by Django 2.1.2 on 2018-10-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0005_workerstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerstatus',
            name='status',
            field=models.CharField(choices=[('Cannot connect', 'Cannot connect'), ('Working', 'Working'), ('Idle', 'Idle')], default='Cannot connect', max_length=5),
        ),
    ]
