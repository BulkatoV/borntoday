# Generated by Django 5.1.6 on 2025-03-20 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star', '0003_alter_star_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='categories',
            field=models.ManyToManyField(related_name='stars', to='star.category', verbose_name='Виды деятельности'),
        ),
        migrations.AlterField(
            model_name='star',
            name='content',
            field=models.TextField(verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='star',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stars', to='star.country', verbose_name='Связанные страны'),
        ),
        migrations.AlterField(
            model_name='star',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя знаменитости'),
        ),
    ]
