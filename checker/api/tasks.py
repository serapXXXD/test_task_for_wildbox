from celery import shared_task
import requests
from datetime import datetime
from .models import UrlData


@shared_task
def check_url_status(url_data_obj):
    status_code = requests.get(url_data_obj.url, timeout=5).status_code
    url_data_obj['status_code'] = status_code
    url_data_obj['checked_at'] = datetime.now()
    url_data_obj.save()
