# Generated by Django 2.2 on 2020-07-25 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200725_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-timestamp', '-updated']},
        ),
    ]
