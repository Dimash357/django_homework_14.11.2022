# Generated by Django 4.1.3 on 2022-11-24 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0010_todocomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoComment',
        ),
    ]