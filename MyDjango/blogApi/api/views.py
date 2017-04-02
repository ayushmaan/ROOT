from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView , DestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import BookSerializer ,BookCreateSerializer
from .models import Books
from rest_framework.permissions import (
 AllowAny,
IsAuthenticated,
IsAuthenticatedOrReadOnly,
IsAdminUser
)


class ApiListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class ApiCreateView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(WhoUpdated = self.request.user)


class ApiDetailView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer




class ApiDestroyView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer



class ApiUpdateView(RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(WhoUpdated=self.request.user)







# Create your views here.

