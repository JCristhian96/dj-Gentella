from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
# Models
from apps.products.models import Category, SubCategory, Mark, Product, MeasureUnit


class StateView(View):
    """  """
    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        model = kwargs['model']
        if model == 'Categoria':
            obj = get_object_or_404(Category, slug=slug)
            
        if model == 'SubCategoria':
            obj = get_object_or_404(SubCategory, slug=slug)
            
        if model == 'Marca':
            obj = get_object_or_404(Mark, slug=slug)
            
        if model == 'Producto':
            obj = get_object_or_404(Product, slug=slug)
        
        if model == 'UMedida':
            model = "Unidad de Medida"
            obj = get_object_or_404(MeasureUnit, slug=slug)
            
        # Cambio de valor de estados
        if obj.active:
            obj.active = False
            messages.warning(request, f"{model} ({obj.title}) desactivado(a)")
        else:
            obj.active = True
            messages.success(request, f"{model} ({obj.title}) reactivado(a)")
        obj.save()
        # 
        return redirect(request.META.get('HTTP_REFERER'))