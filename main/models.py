from django.db import models

class Image_Theme(models.Model):
    image_theme_id = models.CharField(max_length= 30, unique= True)
    image_theme = models.ImageField(upload_to= 'images_theme', blank = True)
    condition = models.CharField(max_length = 20, null = True)
