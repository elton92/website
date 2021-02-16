from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Tema(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Publicar(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
    sub_titulo = models.CharField("Subtitulo", max_length=200, null=True, blank=True)
    imagem = models.ImageField("Imagem", null=True, blank=True, upload_to="images", default="/placeholder2.png")
    conteudo = RichTextUploadingField("Conteudo", null=True, blank=True)
    # conteudo = RichTextField(null=True, blank=True)
    data_criar = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)
    destacar = models.BooleanField(default=False)
    temas = models.ManyToManyField(Tema, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.titulo)

            has_slug = Publicar.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.titulo) + '-' + str(count)
                has_slug = Publicar.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
