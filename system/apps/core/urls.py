from django.urls import path, re_path
# Views
from . import views

urlpatterns = [
    path(
        '',
        views.Index.as_view(),
        name="index"
    ),
    re_path(
        r'^.*\.html', 
        views.Gentella_html.as_view(), 
        name='gentella'
    ),
]
