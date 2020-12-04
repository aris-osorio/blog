# Generated by Django 2.2.14 on 2020-12-04 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('texto', models.CharField(max_length=200)),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.Publicacion')),
            ],
        ),
    ]