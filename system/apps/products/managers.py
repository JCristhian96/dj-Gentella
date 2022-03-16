from django.db import models
from django.db.models import Count


class CategoryManager(models.Manager):
    
    def order_default(self):
        return self.order_by('-active', 'title')
    
    def count_subcategorys(self):
        return self.order_default().annotate(
            count=Count('subcategory')
        )

    def only_actives(self):
        return self.order_default().filter(active=True)
    

class SubCategoryManager(models.Manager):
    
    def related(self):
        return self.select_related('category')
    
    def order_default(self):
        return self.related().order_by('-active', 'title', 'category__title')
    
    def only_category_actives(self):
        return self.order_default().filter(
            category__active=True
        )
        
    def count_products(self):
        return self.only_category_actives().annotate(
            count=Count('product')
        )
        
    def only_actives(self):
        return self.only_category_actives().filter(active=True)


class MeasureUnitManager(models.Manager):
    
    def order_default(self):
        return self.order_by('-active', 'title')
    
    def count_products(self):
        return self.order_default().annotate(
            count=Count('product')
        )
        
    def only_actives(self):
        return self.order_default().filter(active=True)


class MarkManager(models.Manager):
    
    def order_default(self):
        return self.order_by('-active', 'title')
    
    def count_products(self):
        return self.order_default().annotate(
            count=Count('product')
        )
        
    def only_actives(self):
        return self.order_default().filter(active=True)
        

class ProductManager(models.Manager):
    
    def related(self):
        return self.select_related(
            'subcategory__category', 'subcategory', 'mark', 'umedida'
        )
    
    def order_default(self):
        return self.related().order_by('-active', 'title', 'mark__title')
    
    def only_actives_fk(self):
        return self.order_default().filter(
            subcategory__category__active=True,
            subcategory__active=True,
            mark__active=True,
            umedida__active=True
        )
        
    def only_actives(self):
        return self.only_actives_fk().filter(active=True)
        