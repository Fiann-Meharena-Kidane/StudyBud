# Generated by Django 4.1.1 on 2022-10-02 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='anme',
            new_name='name',
        ),
    ]
