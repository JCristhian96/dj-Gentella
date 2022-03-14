from django.views.generic import TemplateView, View
from django.shortcuts import render


class Index(TemplateView):
    template_name = "core/index.html"
    

class Gentella_html(View):
    
    def get(self, request, *args, **kwargs):
        load_template = request.path.split('/')[-1]
        return render(request, f'core/{load_template}')
