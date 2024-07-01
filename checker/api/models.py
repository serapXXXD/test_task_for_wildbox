from django.db import models


class UrlChecker(models.Model):
    url = models.URLField()
    status_code = models.IntegerField(null=True, blank=True)
    date_time_check = models.DateTimeField(auto_now_add=True)


