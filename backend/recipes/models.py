from django.core.validators import MinValueValidator
from django.db import models

from users.models import User

NUMBER_OF_LETTERS: int = 15
MAX_LENTH: int = 200


class Ingredients(models.Model):
    """Модель для хранения данных Ингредиенты."""

    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENTH,
        null=False
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=MAX_LENTH,
        null=False
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Tags(models.Model):
    """Модель для хранения данных Теги."""

    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENTH,
        unique=True,
        null=False
    )
    color = models.CharField(
        verbose_name='Цвет',
        unique=True,
        null=False,
        max_length=7
    )
    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
        null=False
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Recipes(models.Model):
    """Модель для хранения данных Рецепты."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Автор',
        null=False
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_LENTH,
        null=False
    )
    image = models.ImageField(
        upload_to='recipes/images/',
        verbose_name='Картинка',
        null=False
    )
    text = models.TextField(
        verbose_name='Описание',
        null=False
    )
    ingredients = models.ManyToManyField(
        Ingredients,
        through='IngredientsRecipe',
    )
    tags = models.ManyToManyField(
        Tags,
        through='TagsRecipe',
    )
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[MinValueValidator(1)],
        null=False
    )
    pub_date = models.DateTimeField(
        'Время публикации',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        return self.text[:NUMBER_OF_LETTERS]


class IngredientsRecipe(models.Model):
    """ Модель связи ингредиентов и рецепта. """

    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    amount = models.IntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_name_recipe_ingredient'
            )
        ]


class TagsRecipe(models.Model):
    """ Модель связи тегов и рецепта. """

    tags = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)


class Favorite(models.Model):
    """ Модель избранного. """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = "Избранное"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "recipe"),
                name="unique_name_user_recipe"
            )
        ]


class ShoppingCart(models.Model):
    """ Модель списка покупок. """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='shopping_cart',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        related_name='shopping_cart',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_name_user_shoppingcart'
            )
        ]
