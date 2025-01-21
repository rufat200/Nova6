from rest_framework import serializers
from .models import Category, Publication


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created', 'updated']