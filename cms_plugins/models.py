from django.db import models
from cms.models.pluginmodel import CMSPlugin

class CarouselPluginModel(CMSPlugin):
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title or "Custom Carousel"
    

class SlidePluginModel(CMSPlugin):
    image = models.ImageField(upload_to='slides/')
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.caption or "Slide"
    
# Modèle pour la vidéo d'introduction
class VideoIntro(CMSPlugin):
    video_url = models.URLField(verbose_name=("URL de la vidéo"))
    button_text = models.CharField(max_length=50, default="Regarder notre impact")

class Engagement(CMSPlugin):
    icon = models.CharField(max_length=50, verbose_name=("Icône"))
    title = models.CharField(max_length=100, verbose_name=("Titre"))
    description = models.TextField(verbose_name=("Description"))

class Result(CMSPlugin):
    title = models.CharField(max_length=100, verbose_name=("Titre"))
    count = models.PositiveIntegerField(verbose_name=("Chiffre"))

class Testimonial(CMSPlugin):
    name = models.CharField(max_length=100, verbose_name=("Nom"))
    photo = models.ImageField(upload_to='testimonials/', verbose_name=("Photo"))
    quote = models.TextField(verbose_name=("Citation"))

class News(CMSPlugin):
    title = models.CharField(max_length=200, verbose_name=("Titre"))
    date = models.DateTimeField(verbose_name=("Date"))
    content = models.TextField(verbose_name=("Contenu"))
    
# Modèle pour les actualités
class News(CMSPlugin):
    title = models.CharField(max_length=200, verbose_name=("Titre"))
    date = models.DateTimeField(verbose_name=("Date"))
    content = models.TextField(verbose_name=("Contenu"))