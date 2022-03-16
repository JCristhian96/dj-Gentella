from django.contrib import admin
# Models
from .models import Category, SubCategory, Mark, Product, MeasureUnit


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    # fields = ['active', 'title']
    list_display = ('title', 'slug', 'active', 'user_created')
    list_filter = ('active', 'user_created')
    ordering = ('-active', 'title',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    '''Admin View for SubCategory'''

    # fields = ['active', 'title']
    list_display = ('title', 'category', 'slug', 'active')
    list_filter = ('active',)
    ordering = ('-active', 'title',)


@admin.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    '''Admin View for MeasureUnit'''

    fields = ['title', 'active']
    list_display = ('title', 'slug', 'active')
    list_filter = ('active',)
    ordering = ('-active', 'title',)    
    
    
@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    '''Admin View for Mark'''

    # fields = ['active', 'title']
    list_display = ('title', 'slug', 'active')
    list_filter = ('active',)
    ordering = ('-active', 'title',)
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''
    
    save_as = True
    # fields = ['active', 'title']
    list_display = ('title', 'slug', 'subcategory', 'active')
    list_filter = ('active',)
    ordering = ('-active', 'title',)
