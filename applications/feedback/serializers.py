from rest_framework import serializers

from applications.feedback.models import Comment, Favorite, Like, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        models = Comment
        fields = '__all__'


# class LikeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         models = Like
#         fields = '__all__'
