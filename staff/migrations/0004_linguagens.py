# Generated by Django 5.0.3 on 2024-03-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_funcionarios_email_funcionarios_idade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linguagens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
    ]