# Generated by Django 4.2.1 on 2023-05-16 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod_blog', '0004_alter_postmodel_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]