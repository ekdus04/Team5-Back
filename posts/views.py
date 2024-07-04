from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status, viewsets, filters
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from posts.permissions import IsOwner, OnlyRead


# 검색(전체), 검색(post_id), 검색(color) 게시, 수정, 삭제
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner|OnlyRead]
    filter_backends = [filters.SearchFilter]
    search_fields = ['color']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    