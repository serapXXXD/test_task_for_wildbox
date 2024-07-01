from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
import json
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from .models import UrlData
from .serializer import UrlDataSerializer, UrlDataListSerializer


class UrlCheckerViewSet(viewsets.ModelViewSet):
    queryset = UrlData.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UrlDataSerializer

    @action(detail=False, methods=['POST'], serializer_class=UrlDataListSerializer)
    def bulk_create(self, request):
        serializer = UrlDataListSerializer(data=request.data)
        if serializer.is_valid():
            items = serializer.save()
            interval, int_created = IntervalSchedule.objects.get_or_create(
                every=5, period="minutes"
            )

            for item in items:
                task, created = PeriodicTask.objects.get_or_create(
                    name="check_url_status", interval=interval
                )
                kwargs = {
                    "url": item.url
                }
                task.kwargs = json.dumps(kwargs)
                task.one_off = True
                task.enabled = True
                task.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
