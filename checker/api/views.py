from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import UrlData
from .serializer import UrlDataSerializer, UrlDataListSerializer


class UrlCheckerViewSet(viewsets.ModelViewSet):
    queryset = UrlData.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UrlDataSerializer

    @action(detail=False, methods=['POST'], serializer_class=UrlDataListSerializer)
    def bulk_create(self, request):
        serializer = UrlDataListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
