# Generated by Django 4.1.6 on 2023-04-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Title',
            field=models.CharField(max_length=101),
        ),
    ]
