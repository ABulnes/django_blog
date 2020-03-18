from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre de Categoria', max_length=200, blank=False, null=False)
    state = models.BooleanField('Categoria Activada/Categoria No Activada', default=True)
    creation_date = models.DateField('Fecha de creacion',auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField('Nombre de autor', max_length=255, null=False, blank=False)
    last_names = models.CharField('Apellidos de autor', max_length=255, null=False, blank=False)
    facebook = models.URLField('Facebook', null=True,blank=True)
    twitter = models.URLField('Twitter', null=True,blank=True)
    instagram = models.URLField('Instagram', null=True,blank=True)
    web = models.URLField('Página web', null=True,blank=True)
    email = models.EmailField('Correo', blank=False, null=False)
    state = models.BooleanField('Autor Activo/No activo', default=True)
    creation_date = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.last_names,self.names)


class Post(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField('Descripción', max_length=110, blank=True, null=True)
    content = RichTextField()
    image = models.URLField('Imagen', blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    state = models.BooleanField('Publicado/No Publicado', default=True)
    creation_date = models.DateField('Fecha de creación', auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
