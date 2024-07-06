from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from game.models import Game

from game.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [AllowAny]