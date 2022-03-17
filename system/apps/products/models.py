from django.db import models
from django.db.models.signals import pre_save
# Models
from apps.core.models import TimeStampedModel
# Easy Thumbnails
from easy_thumbnails.fields import ThumbnailerImageField
# Signals, Managers
from . import signals, managers


class Category(TimeStampedModel):
    """ Modelo para el manejo de las Categorias de un producto """
    
    title = models.CharField(max_length=100, unique=True, verbose_name="Titulo",
        error_messages={"unique":"Categoria ya regitrada."})
    
    objects = models.Manager()
    objects_plus = managers.CategoryManager()
        

class SubCategory(TimeStampedModel):
    """ Modelo para el manejo de las Sub Categorias de un producto """
    
    title = models.CharField(max_length=100, verbose_name="Titulo")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    
    objects = models.Manager()
    objects_plus = managers.SubCategoryManager()
    
    def __str__(self):
        return f"{self.title}-{self.category.title}"
                
    class Meta:
        unique_together = ('title', 'category',)


class MeasureUnit(TimeStampedModel):
    """ Modelo para el manejo de las Unidades de Medida de un producto """
    
    title = models.CharField(max_length=100, unique=True, verbose_name="Titulo",
        error_messages={"unique":"Unidad de Medida ya regitrada."})
    
    objects = models.Manager()
    objects_plus = managers.MeasureUnitManager()
                

class Mark(TimeStampedModel):
    """ Modelo para el manejo de las Marcas de un producto """
    
    title = models.CharField(max_length=100, unique=True, verbose_name="Titulo",
        error_messages={"unique":"Marca ya regitrada."})    
    image = ThumbnailerImageField(upload_to="marks/", null=True, blank=True, verbose_name="Imagen")
    
    objects = models.Manager()
    objects_plus = managers.MarkManager()

    
class Product(TimeStampedModel):
    """ Modelo para el manejo de los Productos """
    
    cod_barra = models.CharField(max_length=255, unique=True, editable=False)
    title = models.CharField(max_length=100, verbose_name="Titulo")
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name='Marca')
    model = models.CharField(max_length=100, verbose_name="Modelo", default="Generico")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='SubCategoria')
    umedida = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    
    detail = models.TextField(blank=True, null=True, verbose_name="Detalles")
    price = models.DecimalField(default=0.0, max_digits=11, decimal_places=2, verbose_name="Precio")
    reduction = models.DecimalField(default=0.0, max_digits=11, decimal_places=2, verbose_name="Rebaja")
    stock = models.IntegerField(default=0)
    image = ThumbnailerImageField(upload_to="products/", null=True, blank=True, verbose_name="Imagen")
    
    objects = models.Manager()
    objects_plus = managers.ProductManager()
    
    def clean(self):
        self.title = self.title.title()
        self.model = self.model.title()
        return super().clean()
    
    class Meta:
        unique_together = ('title', 'mark',)

# Signals
pre_save.connect(signals.set_slug, sender=Category)
pre_save.connect(signals.set_slug, sender=Mark)
pre_save.connect(signals.set_slug, sender=MeasureUnit)
pre_save.connect(signals.set_cod_barra_slug, sender=Product)
pre_save.connect(signals.set_slug_subcategory, sender=SubCategory)