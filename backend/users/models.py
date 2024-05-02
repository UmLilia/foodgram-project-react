from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Кастомная модель пользователя. """

    username = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='Введите адрес эл.почты',
        unique=True
    )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True,
        null=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscriptions(models.Model):
    """ Модель подписок. """

    user = models.ForeignKey(
        User,
        related_name='subscriptions',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Подписки"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "author"),
                name="unique_name_user_author"
            )
        ]
