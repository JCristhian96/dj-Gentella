from django.urls import path
# Views
from .views import (
    BaseViews, CategoryViews, SubCategoryViews, MarkViews, ProductViews, MeasureUniteViews
)

app_name = "products"

urlpatterns = [
    # Urls Categorias
    path('categorys/', CategoryViews.CategoryListView.as_view(), name="categorys"),
    path('category/add/', CategoryViews.CategoryCreateView.as_view(), name="category_add"),
    path('category/update/<slug:slug>/', CategoryViews.CategoryUpdateView.as_view(), name="category_update"),

    # Urls SubCategorias
    path('subcategorys/', SubCategoryViews.SubCategoryListView.as_view(), name="subcategorys"),
    path('subcategory/add/', SubCategoryViews.SubCategoryCreateView.as_view(), name="subcategory_add"),
    path('subcategory/update/<slug:slug>/', SubCategoryViews.SubCategoryUpdateView.as_view(), name="subcategory_update"),
    
    # Urls Unidades de Medida
    path('measureunits/', MeasureUniteViews.MeasureUnitListView.as_view(), name="measureunits"),
    path('measureunits/add/', MeasureUniteViews.MeasureUnitCreateView.as_view(), name="measureunit_add"),
    path('measureunits/update/<slug:slug>/', MeasureUniteViews.MeasureUnitUpdateView.as_view(), name="measureunit_update"),

    # Urls Marcas
    path('marks/', MarkViews.MarkListView.as_view(), name="marks"),
    path('mark/add/', MarkViews.MarkCreateView.as_view(), name="mark_add"),
    path('mark/update/<slug:slug>/', MarkViews.MarkUpdateView.as_view(), name="mark_update"),

    # Urls Productos
    path('products/', ProductViews.ProductListView.as_view(), name="products"),
    path('product/add/', ProductViews.ProductCreateView.as_view(), name="product_add"),
    path('product/update/<slug:slug>/', ProductViews.ProductUpdateView.as_view(), name="product_update"),
    
    # Urls Control de estados
    path('state/<slug:model>/<slug:slug>/', BaseViews.StateView.as_view(), name="state"),
]
