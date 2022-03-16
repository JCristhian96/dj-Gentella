from django.urls import reverse_lazy
# Models
from apps.products.models import SubCategory
# Forms
from apps.products.forms import SubCategoryForm
# Mixins
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView


class SubCategoryListView(BaseListView):
    """  """
    model = SubCategory
    template_name = "products/subcategorys.html"
    
    def get_queryset(self):
        return SubCategory.objects_plus.count_products()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub Categorias"
        context["url_add"] = reverse_lazy("products:subcategory_add")
        context["model"] = "SubCategoria"
        return context
    

class SubCategoryCreateView(BaseCreateView):
    """  """
    model = SubCategory
    template_name = "core/bases/base_form.html"
    success_message = 'Sub Categoria creada exitosamente'
    success_url = reverse_lazy('products:subcategorys')
    form_class = SubCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva SubCategoria"
        context['url_list'] = self.success_url
        return context


class SubCategoryUpdateView(BaseUpdateView):
    """  """
    model = SubCategory
    template_name = "core/bases/base_form.html"
    success_message = 'Sub Categoria actualizada exitosamente'
    success_url = reverse_lazy('products:subcategorys')
    form_class = SubCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar SubCategoria"
        context['url_list'] = self.success_url
        return context
    

