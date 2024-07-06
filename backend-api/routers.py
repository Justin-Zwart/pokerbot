from rest_framework import routers

from game.viewsets import GameViewSet

router = routers.SimpleRouter()

router.register(r'game', GameViewSet, basename="game")

urlpatterns = router.urls