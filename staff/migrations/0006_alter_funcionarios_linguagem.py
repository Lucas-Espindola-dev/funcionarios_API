# Generated by Django 5.0.3 on 2024-03-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_funcionarios_linguagem_remove_funcionarios_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='linguagem',
            field=models.ManyToManyField(to='staff.linguagens'),
        ),
    ]
