# Generated by Django 3.2.17 on 2023-04-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0017_alter_resume_matchpercentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='short',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]