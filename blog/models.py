from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField('Sarlavha', max_length=255 , db_index=True)
    # slug = models.SlugField('Manzil' , max_length=255 , unique=True),
    description = models.TextField("Izoh" , blank=True , db_index=True)
    image = models.ImageField('Rasm' , db_index=True)
    date = models.DateTimeField('Sana' , default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
