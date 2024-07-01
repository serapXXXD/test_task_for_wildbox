from rest_framework import serializers
from .models import UrlData


# class UrlDataListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         urls = [UrlData(**url) for url in validated_data]
#         return UrlData.objects.bulk_crteate(urls)


class UrlDataSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    status_code = serializers.IntegerField(read_only=True)
    checked_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UrlData
        fields = '__all__'


class UrlDataListSerializer(serializers.ModelSerializer):
    url_list = serializers.ListField(child=serializers.URLField())

    def create(self, validated_data):
        urls = [UrlData(url=url) for url in validated_data.pop('url_list')]

        return UrlData.objects.bulk_create(urls)

    def to_representation(self, items):
        return {'url_list': [{'id': item.id, 'url': item.url} for item in items]}

    class Meta:
        model = UrlData
        fields = ('url_list',)
