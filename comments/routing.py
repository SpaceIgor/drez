from django.urls import path

from django_spa_comments import consumers

websocket_urlpatterns = [
    path(r"ws/comments/", consumers.CommentsConsumer.as_asgi()),
]