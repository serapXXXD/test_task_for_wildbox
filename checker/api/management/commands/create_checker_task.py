from django.core.management import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    help = "Создаёт переодическую задачу для проверки Url'ов"

    def handle(self, *args, **options):
        interval, _ = IntervalSchedule.objects.get_or_create(
            every=5, period="minutes")
        task, _ = PeriodicTask.objects.get_or_create(
            name="check_url_status", interval=interval,
            task='api.tasks.check_url_status'
        )
        task.enabled = True
        task.save()
        self.stdout.write(self.style.SUCCESS('Задача создана.'))


