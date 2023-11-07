# Generated by Django 4.2.7 on 2023-11-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
