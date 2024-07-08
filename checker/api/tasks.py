from celery import shared_task
import requests
from datetime import datetime
from .models import UrlData


@shared_task
def check_url_status():
    urls = UrlData.objects.filter(status_code=None)
    for url in urls:
        try:
            # with open(f'url{url.id}', 'w') as file:
            #     file.write(url.url)
            response = requests.get(url.url, timeout=5)
            url.status_code = response.status_code
            url.checked_at = datetime.now()
            url.save()
        except (requests.ConnectionError, requests.RequestException):
            continue

# docker exec -it checker_infra_backend_1 python manage.py create_checker_task