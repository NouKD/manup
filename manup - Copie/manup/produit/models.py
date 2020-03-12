from django.db import models

# Create your models here.

class Temoignage(models.Model):
    ICONES = [
        ('facebook', 'fab fa-facebook'),
        ('instagrame', 'fab fa-instagram'),
        ('twitter', 'fa fa-twitter'),
        ('linkedin', 'fab fa-linkedin-in'), 
    ]
    nom = models.CharField(max_length = 255)
    prenom = models.CharField(max_length = 255)
    liens = models.URLField()
    icone = models.CharField(choices=ICONES, max_length=20)
    image = models.ImageField(upload_to='images Temoignage')
    comentaire = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name = "Temoignage"
        verbose_name_plural =  "Temoignages"

    def __str__(self):
        return self.nom

class sponsor(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images Temoignage')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="sponsor"
        verbose_name_plural = "sponsors"

    def __str__(self):
        return self.nom  

class SiteInfo(models.Model):
    map_url = models.TextField()
    email = models.EmailField()
    logo = models.ImageField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Site Info"
        verbose_name_plural = "Site Infos"

    def __str__(self):
        return self.email               

