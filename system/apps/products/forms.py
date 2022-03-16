from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
# Models
from .models import Category, SubCategory, Mark, Product, MeasureUnit


class BaseForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['autofocus'] = True
        

class CategoryForm(BaseForm):
    
    class Meta:
        model = Category
        fields = ["title", "active"]
                
        
class MarkForm(BaseForm):
    
    class Meta:
        model = Mark
        fields = ["title", "image", "active"]


class MeasureUnitForm(BaseForm):
    
    class Meta:
        model = MeasureUnit
        fields = ["title", "active"]
        
        
class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        # fields = ("title", "active", "mark", "")
        fields = (
            "title", "mark", "model", "subcategory", "umedida", "detail",
            "price", "reduction", "stock", "image", "active"   
        )
        
        # fields = ["title", "category", "active"]
        # exclude = ("user_created", "user_modified",)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Ya existe un Producto registrado con esta Marca",
            }
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['mark'].queryset = Mark.objects_plus.only_actives()
        self.fields['subcategory'].queryset = SubCategory.objects_plus.only_actives()
        self.fields['umedida'].queryset = MeasureUnit.objects_plus.only_actives()
        self.fields['title'].widget.attrs['autofocus'] = True
    

class SubCategoryForm(forms.ModelForm):
    
    class Meta:
        model = SubCategory
        fields = ["title", "category", "active"]
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Titulo de SubCategoria ya registrado en Categoria seleccionada",
            }
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['category'].queryset = Category.objects_plus.only_actives()
        self.fields['title'].widget.attrs['autofocus'] = True