from django.urls import reverse_lazy
# Models
from apps.products.models import Product
# Forms
from apps.products.forms import ProductForm
# Mixins
from apps.core.views import BaseListView, BaseCreateView, BaseUpdateView


class ProductListView(BaseListView):
    """  """
    # model = Product
    template_name = "products/products.html"
    
    def get_queryset(self):
        return Product.objects_plus.only_actives_fk()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model"] = "Producto"
        context["title"] = "Productos"
        context["url_add"] = reverse_lazy("products:product_add")
        return context
    

class ProductCreateView(BaseCreateView):
    """  """
    form_class = ProductForm
    model = Product
    success_message = 'Producto creado exitosamente'
    success_url = reverse_lazy('products:products')
    template_name = "core/bases/base_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Producto"
        context['url_list'] = self.success_url
        return context
    

class ProductUpdateView(BaseUpdateView):
    """  """
    form_class = ProductForm
    model = Product
    success_message = 'Producto actualizado exitosamente'
    success_url = reverse_lazy('products:products')
    template_name = "core/bases/base_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Producto"
        context['url_list'] = self.success_url
        return context
