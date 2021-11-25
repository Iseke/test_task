from django.db import models
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_('Название')
    )
    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Дата старта')
    )
    end_date = models.DateField(
        verbose_name=_('Дата окончания')
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Описание')
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name=_('Дата создания')
    )
    updated_at = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name=_('Дата изменения')
    )

    def __str__(self):
        return f'{self.name} -- {self.start_date} -- {self.end_date}'
