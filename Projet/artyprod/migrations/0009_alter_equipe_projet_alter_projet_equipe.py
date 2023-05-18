# Generated by Django 4.2.1 on 2023-05-13 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artyprod', '0008_alter_equipe_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='projet',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipes', to='artyprod.projet'),
        ),
        migrations.AlterField(
            model_name='projet',
            name='equipe',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projets', to='artyprod.equipe'),
        ),
    ]