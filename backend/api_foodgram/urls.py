from django.urls import include, path
from rest_framework import routers

from .views import (FavoriteView, IngredientsViewSet, RecipesViewSet,
                    ShoppingCartView, SubscribeView, SubscriptionsViewSet,
                    TagsViewSet, download_shopping_cart)

app_name = 'api_foodgram'

router = routers.DefaultRouter()

router.register(r'ingredients', IngredientsViewSet)
router.register(r'tags', TagsViewSet)
router.register(r'recipes', RecipesViewSet)
router.register(
    r'users/subscriptions',
    SubscriptionsViewSet,
    basename='subscriptions'
)


urlpatterns = [
    path(
        'recipes/download_shopping_cart/',
        download_shopping_cart,
        name='download_shopping_cart'
    ),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path(
        'users/<int:id>/subscribe/',
        SubscribeView.as_view(),
        name='subscribe'
    ),
    path(
        'recipes/<int:id>/favorite/',
        FavoriteView.as_view(),
        name='favorite'
    ),
    path(
        'recipes/<int:id>/shopping_cart/',
        ShoppingCartView.as_view(),
        name='shopping_cart'
    ),
]
