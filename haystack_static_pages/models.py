# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _


class StaticPage(models.Model):
    title = models.CharField(_('title'), max_length=255)
    url = models.CharField(_('url'), max_length=255, blank=True, null=True)
    description = models.TextField(_('description'), blank=True)
    content = models.TextField(_('content'))
    language = models.CharField(_('language'), max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = _('static page')
        verbose_name_plural = _('static pages')

    def __repr__(self):
        return '<StaticPage: %s>' % self.url

    def __unicode__(self):
        return force_unicode(self.__repr__())

    def get_absolute_url(self):
        return self.url

    def search(self):
        return dict(source=_(u'Static'), title=self.title, desc=self.content)
