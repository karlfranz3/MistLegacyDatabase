# Generated by Django 3.2.7 on 2021-10-31 15:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('front', '0065_rename_spell_talent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Component',
        ),
    ]
