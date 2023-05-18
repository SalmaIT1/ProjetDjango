# Generated by Django 4.2.1 on 2023-05-13 00:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artyprod', '0006_contact_remove_equipe_membres_remove_equipe_projet_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='personne',
        ),
        migrations.AddField(
            model_name='equipe',
            name='membres',
            field=models.ManyToManyField(related_name='equipes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipe',
            name='projet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='equipes', to='artyprod.projet'),
        ),
        migrations.AddField(
            model_name='projet',
            name='equipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='projets', to='artyprod.equipe'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='nom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='projet',
            name='acheve',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projet',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
