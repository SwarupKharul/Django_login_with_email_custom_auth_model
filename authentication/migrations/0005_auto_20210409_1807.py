# Generated by Django 3.1.1 on 2021-04-09 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Idea',
        ),
    ]
