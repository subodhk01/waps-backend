from django.shortcuts import render
from rest_framework import status,mixins,generics
from rest_framework import viewsets
from .serializers import FeedViewSerializer
from .models import Book


# Create your views here.



class feedView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=FeedViewSerializer
    queryset=Book.objects.all()


