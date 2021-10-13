'''Fix for `ContentType` translations issue'''
from django.apps import apps
from django.contrib.contenttypes.models import ContentType


def new_app_labeled_name(self):
    '''ContentTypes translation problem could be
        solved by use `model._meta.verbose_name`
        if `verbose_name` has been defined in Models Meta class and
        the name have to be marked for translation
    '''
    if self.model_class():
        return '{0} | {1}'.format(self.model_class()._meta.verbose_name,
                                  apps.get_app_config(self.model_class(
                                  )._meta.app_label).verbose_name)


def class_decorator(cls):
    '''Class patcher function'''
    cls.app_labeled_name = property(new_app_labeled_name)
    return cls


# patch the ContentType class
class_decorator(ContentType)
