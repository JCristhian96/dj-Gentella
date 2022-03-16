from django.urls import reverse_lazy
# Models
from apps.products.models import MeasureUnit
# Forms
from apps.products.forms import MeasureUnitForm
# Mixins
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView


class MeasureUnitListView(BaseListView):
    """  """
    template_name = "products/measureunits.html"
    
    def get_queryset(self):
        return MeasureUnit.objects_plus.count_products()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Unidad de Medida"
        context["url_add"] = reverse_lazy("products:measureunit_add")
        context["model"] = "UMedida"
        return context
    

class MeasureUnitCreateView(BaseCreateView):
    """  """
    form_class = MeasureUnitForm
    model = MeasureUnit
    success_message = 'Unidad de Medida creada exitosamente'
    success_url = reverse_lazy('products:measureunits')
    template_name = "core/bases/base_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Unidad de Medida"
        context['url_list'] = self.success_url
        return context
    

class MeasureUnitUpdateView(BaseUpdateView):
    """  """
    form_class = MeasureUnitForm
    model = MeasureUnit
    success_message = 'Unidad de Medida actualizada exitosamente'
    success_url = reverse_lazy('products:measureunits')
    template_name = "core/bases/base_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Unidad de Medida"
        context['url_list'] = self.success_url
        return context
