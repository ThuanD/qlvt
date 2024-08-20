import os
from hashlib import md5

from django.db import models
from django.utils.text import slugify as _slugify
from django.utils.translation import gettext_lazy as _


def customers_contract(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        f'{md5(filename.encode()).hexdigest()}/{_slugify(instance.name)}{ext}'
    )


class Contract(models.Model):
    name = models.CharField(_('name'), max_length=100)
    contract = models.ImageField(_('contract'), upload_to=customers_contract)
    ctime = models.DateTimeField(_('Created time'), auto_now_add=True)
    mtime = models.DateTimeField(_('Modified time'), auto_now=True)

    class Meta:
        db_table = 'contract'
        verbose_name = _('contract')
        permissions = (
            ('import_folder', _('Can import contract')),
            ('export_folder', _('Can export contract')),
        )

    def __str__(self):
        return self.name
