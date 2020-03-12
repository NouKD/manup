from django.db import models

# Create your models here.

class presentation(models.Model):
    ICONES = [
        ('facebook', 'fab fa-facebook'),
        ('twitter', 'fa fa-twitter'),
        ('linkedin', 'fab fa-linkedin-in'),
        ('instagrame', 'fab fa-instagram'),
        ('youtube', 'fa fa-youtube-play'),
    ]
    nom = models.CharField(max_length=255)
    liens = models.URLField()
    icone = models.CharField(choices=ICONES, max_length=20)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/presentation')
    status = models.CharField(max_length=255)
    titre = models.CharField(max_length=255) 
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="presentation"
        verbose_name_plural = "presentations"

    def __str__(self):
        return self.nom         

class Programme(models.Model):
    nom = models.CharField(max_length = 255)
    prix = models.FloatField
    image = models.ImageField(upload_to='images/Programme')
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Programme"
        verbose_name_plural = "Programmes"

    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.nom 

class Article(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    contenue = models.TextField()
    image = models.ImageField(upload_to='images/Article')
    tag = models.ManyToManyField(Tag,related_name="Tag_Article")
    categorie = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='Article')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default = True)

    class Meta:
        verbose_name ="Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.nom         

