from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для группы"""
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        help_text='Дайте название группе'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Адрес для страницы группы',
        help_text=(
            'Укажите адрес для страницы группы. '
            'Используйте только латиницу, цифры, '
            'дефисы и знаки подчёркивания'
        )
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Укажите описание группы.'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для поста"""
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Напишите текст поста'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True, blank=True,
        verbose_name='Картинка',
        help_text='Добавьте картинку'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name='Группа',
        help_text='Выберите группу'
    )

    def __str__(self):
        """Вывод поста по текстовой строке"""
        return self.text


class Comment(models.Model):
    """Модель для комментария"""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите текст комментария'
    )
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )


class Follow(models.Model):
    """Модель для подписки"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            )
        ]
