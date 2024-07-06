from rest_framework import serializers

from game.models import Game

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['name', 'players', 'created', 'updated', 'id']
        read_only_fields = ['created', 'updated', 'id']