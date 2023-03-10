from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.feedback.models import Comment
from applications.feedback.serializers import CommentSerializer


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

