from django.db import models


class UrlData(models.Model):
    url = models.URLField(unique=True)
    status_code = models.IntegerField(null=True, blank=True, verbose_name='Статус код')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    checked_at = models.DateTimeField(null=True, blank=True, verbose_name='Дата проверки')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['-id']
