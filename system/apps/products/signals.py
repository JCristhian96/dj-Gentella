import uuid
from django.utils.text import slugify


def set_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    return instance

def set_slug_subcategory(sender, instance, *args, **kwargs):
    instance.slug = f"{slugify(instance.title)}-{instance.category.slug}"
    return instance

def set_cod_barra_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    instance.slug = f"{instance.slug}-{instance.mark.slug}"
    instance.cod_barra = f"{instance.slug}-{str(uuid.uuid4())[:18]}"
    return instance