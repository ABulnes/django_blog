# Generated by Django 3.0.4 on 2020-03-17 01:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre de Categoria'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=90, verbose_name='Titulo')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('description', models.CharField(blank=True, max_length=110, null=True, verbose_name='Descripción')),
                ('content', ckeditor.fields.RichTextField()),
                ('image', models.URLField(verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Publicado/No Publicado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Categories')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]