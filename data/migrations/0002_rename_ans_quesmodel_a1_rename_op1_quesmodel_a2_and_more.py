# Generated by Django 4.1.5 on 2023-01-15 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='ans',
            new_name='A1',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op1',
            new_name='A2',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op2',
            new_name='A3',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op3',
            new_name='A4',
        ),
        migrations.RenameField(
            model_name='quesmodel',
            old_name='op4',
            new_name='A5',
        ),
    ]
