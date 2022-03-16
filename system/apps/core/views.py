from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, ListView, CreateView, UpdateView


class Index(LoginRequiredMixin, TemplateView):
    template_name = "core/index.html"
    

class Gentella_html(View):
    
    def get(self, request, *args, **kwargs):
        load_template = request.path.split('/')[-1]
        return render(request, f'core/{load_template}')
    
    
class BaseListView(LoginRequiredMixin, ListView):
    template_name = "core/bases/base_list.html"


class BaseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "core/bases/base_form.html"
    
    def form_valid(self, form):
        add_another = self.request.POST.get('add_another', None)        
        if add_another != None:
            self.success_url = "."
        object = form.save(commit=False)
        object.user_created = self.request.user
        object.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):        
        return super().post(request, *args, **kwargs)


class BaseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "core/bases/base_form.html"
    success_message = ""
    
    def form_valid(self, form):
        add_another = self.request.POST.get('add_another', None)             

        if form.has_changed():
            if add_another != None:
                try:
                    form.cleaned_data['title'] = form.cleaned_data['title'].title()
                    form.cleaned_data['user_created'] = self.request.user
                    instance = self.model(**form.cleaned_data)
                    instance.save()
                    messages.success(self.request, f"{instance} creado exitosamente")
                    return redirect(self.success_url)
                except IntegrityError as ex:
                    self.update_form(form)
                
            else:
                self.update_form(form)
        else:
            messages.info(self.request, "Ningun cambio realizado")
        return super().form_valid(form)
    
    
    def update_form(self, form):
        object = form.save(commit=False)
        object.user_modified = self.request.user.id
        object.save()
        messages.success(self.request, self.success_message)