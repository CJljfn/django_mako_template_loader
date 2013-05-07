# -*- coding:utf-8 -*-

import os

from mako.lookup import TemplateLookup 
from django.template.loaders import app_directories
from django.conf import settings
 
from mako import template
 
class DMTemplate(template.Template):
     
    def render(self, context):
        # flatten the Django Context into a single dictionary. 
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return super(DMTemplate, self).render(**context_dict)
     
mylookup = TemplateLookup(
    directories = settings.TEMPLATE_DIRS,
    default_filters=['decode.utf8'],
    # module_directory = os.path.join(settings.TEMPLATE_DIRS[0], 'tmp'),
    input_encoding = 'utf-8',
    output_encoding = 'utf-8',
    encoding_errors = 'replace',
    format_exceptions = True,
)


class Loader(app_directories.Loader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, settings.TEMPLATE_DIRS)
        _template = DMTemplate(text=source, lookup=mylookup)
        return _template,  _template.source
