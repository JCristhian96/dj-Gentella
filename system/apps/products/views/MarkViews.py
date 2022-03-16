from django.urls import reverse_lazy
# Models
from apps.products.models import Mark
# Forms
from apps.products.forms import MarkForm
# Mixins
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView


class MarkListView(BaseListView):
    """  """
    template_name = "products/marks.html"
    
    def get_queryset(self):
        return Mark.objects_plus.count_products()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Marcas"
        context["url_add"] = reverse_lazy("products:mark_add")
        context["model"] = "Marca"
        return context
    

class MarkCreateView(BaseCreateView):
    """  """
    model = Mark
    template_name = "core/bases/base_form.html"
    success_message = 'Marca creada exitosamente'
    success_url = reverse_lazy('products:marks')
    form_class = MarkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Marca"
        context['url_list'] = self.success_url
        return context
    

class MarkUpdateView(BaseUpdateView):
    """  """
    model = Mark
    template_name = "core/bases/base_form.html"
    success_message = 'Marca actualizada exitosamente'
    success_url = reverse_lazy('products:marks')
    form_class = MarkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Marca"
        context['url_list'] = self.success_url
        return context

