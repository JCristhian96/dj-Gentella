# Debug Toolbar
# Shell Plus


def load_setting_devs(*args, **kwargs):    
    INSTALLED_APPS = args[0]
    INSTALLED_APPS.append("debug_toolbar")
    INSTALLED_APPS.append('django_extensions')
    
    MIDDLEWARE = args[1]
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware",)

def set_internal_ips():
    return [
        "127.0.0.1",
    ]