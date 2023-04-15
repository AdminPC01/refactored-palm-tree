# Generated by Django 4.1.6 on 2023-04-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profiles_profile'),
        ('projects', '0002_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Title',
            field=models.CharField(blank=True, max_length=101, null=True),
        ),
    ]
