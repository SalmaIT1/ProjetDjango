# Generated by Django 4.2.1 on 2023-05-18 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0022_user_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='service',
        ),
    ]
