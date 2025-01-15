from rest_framework import generics

from .models import Category
from .serializers import CategorySerializers

# create, get
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

# delete, put
class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

