# Generated by Django 4.0.3 on 2022-03-30 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_publisher_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
