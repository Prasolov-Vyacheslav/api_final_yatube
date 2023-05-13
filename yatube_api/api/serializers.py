from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, User, Follow


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели группы"""
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписка"""
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    def validate(self, data):
        """Проверка подписка сам на себя"""
        if self.context.get('request').user == data['following']:
            raise serializers.ValidationError(
                'Пользователь не может подписаться сам на себя')
        return data

    class Meta:
        fields = ('user', 'following')
        read_only_fields = ('user',)
        model = Follow

        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели поста"""
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария"""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('author', 'post')
        model = Comment
