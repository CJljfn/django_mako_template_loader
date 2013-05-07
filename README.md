django_mako_template_loader
===========================

mako template loader plugin in django


locate the file in your project root directory.
modify the settings file like below:

TEMPLATE_LOADERS = (
    # 'django.template.loaders.filesystem.Loader',
    # 'django.template.loaders.app_directories.Loader',
    'mako_loader.Loader',    # add this
)
