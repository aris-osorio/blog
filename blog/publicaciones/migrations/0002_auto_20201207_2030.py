# Generated by Django 2.2.14 on 2020-12-08 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='tag',
            field=models.ManyToManyField(related_name='publicaciones', to='tags.Tag'),
        ),
    ]
