# Generated by Django 5.1.2 on 2024-10-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emp',
            name='age',
        ),
        migrations.AddField(
            model_name='emp',
            name='address',
            field=models.TextField(default='Unknown address'),
        ),
        migrations.AddField(
            model_name='emp',
            name='department',
            field=models.CharField(default='General', max_length=40),
        ),
        migrations.AddField(
            model_name='emp',
            name='emp_id',
            field=models.CharField(default='EMP123', max_length=100),
        ),
        migrations.AddField(
            model_name='emp',
            name='phone',
            field=models.CharField(default='0000000000', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emp',
            name='working',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
