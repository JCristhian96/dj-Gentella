from django.db import models
# Models
from apps.users.models import User


class TimeStampedModel(models.Model):
    """ Modelo para el manejo de los cambios de los modelos """
    
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    user_created = models.ForeignKey(User, on_delete=models.PROTECT)
    user_modified = models.PositiveIntegerField(null=True, blank=True)
    
    active = models.BooleanField(default=True, verbose_name="Activo")
    slug = models.SlugField(unique=True, blank=False, null= False, editable=False)
    
    def __str__(self):
        return self.title
            
    def clean(self):
        self.title = self.title.title()
        return super().clean()
    class Meta:
        abstract = True

