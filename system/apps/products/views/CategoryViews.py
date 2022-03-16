from django.urls import reverse_lazy
# Models
from apps.products.models import Category
# Forms
from apps.products.forms import CategoryForm
# Mixins
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView


class CategoryListView(BaseListView):
    """  """
    template_name = "products/categorys.html"
    
    def get_queryset(self):
        return Category.objects_plus.count_subcategorys()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categorias"
        context["url_add"] = reverse_lazy("products:category_add")
        context["model"] = "Categoria"
        return context
    

class CategoryCreateView(BaseCreateView):
    """  """
    model = Category
    template_name = "core/bases/base_form.html"
    success_message = 'Categoria creada exitosamente'
    success_url = reverse_lazy('products:categorys')
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Categoria"
        context['url_list'] = self.success_url
        return context
    

class CategoryUpdateView(BaseUpdateView):
    """  """
    model = Category
    template_name = "core/bases/base_form.html"
    success_message = 'Categoria actualizada exitosamente'
    success_url = reverse_lazy('products:categorys')
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Categoria"
        context['url_list'] = self.success_url
        return context
