from os import path

from rest_framework.routers import DefaultRouter
from django.urls import include

from applications.feedback.views import CommentAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)

urlpatterns = router.urls
