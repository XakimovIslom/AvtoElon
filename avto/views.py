from django.shortcuts import render
from rest_framework import generics

from avto.models import Post, District
from avto.serializers import PostSerializer, PostRetrieveSerializer, PostSimilarSerializer, PostSubSerializer, \
    DistrictSerializer, PostFilterSerializer, PostOptionSerializer


# Create your views here.
class MainPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSerializer
    filterset_fields = ("subcategory__category", 'subcategory')


class MainPostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostRetrieveSerializer


class MainPostRetrieveSimilarListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSimilarSerializer


class PostSubListAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-published_at")
    serializer_class = PostSubSerializer
    filterset_fields = ("subcategory",)


class DistrictListAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class FilterPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostFilterSerializer
    filterset_fields = ('district', 'options')