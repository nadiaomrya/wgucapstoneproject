# Generated by Django 4.1.5 on 2023-01-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_rename_ans_quesmodel_a1_rename_op1_quesmodel_a2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('userEmail', models.CharField(max_length=60)),
                ('userPassword', models.CharField(max_length=25)),
            ],
        ),
    ]
