from celery import shared_task
import requests
from datetime import datetime
from .models import UrlData


@shared_task
def check_url_status():
    urls = UrlData.objects.filter(status_code=None)
    for url in urls:
        try:
            response = requests.get(url.url, timeout=5)
            url.status_code = response.status_code
            url.checked_at = datetime.now()
            url.save()
        except (requests.ConnectionError, requests.RequestException):
            continue
