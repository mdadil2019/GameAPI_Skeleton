
from game.models import GameCategory,Game,Player,PlayerScore
from game.serializers import GameCategorySerializer, GameSerializer, PlayerSerializer, PlayerScoreSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

#the API has to support the following endpoints[Game Category, Game, Players, Scores]
# 1. Collection of Game Catogeries[GET,POST]
# 2. Particular Game Category [GET, PUT, PATCH, DELETE]
# 3. Collection of Games[GET, POST]
# 4. Particular Game [GET, PUT, PATCH, DELETE]
# 5. Collection of Players [GET, POST]
# 6. Particular Player [GET, PUT, PATCH, DELETE]
# 7. Collection of Scores [GET, POST]
# 8. Particular score [GET, PUT, PATCH, DELETE] -- Reqired player name

class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'

class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name='game-detail'

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'

class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'

class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request, *args, **kwargs):
        return Response({
            'players' : reverse(PlayerList.name, request = request),
            'game-categories': reverse(GameCategoryList.name, request = request),
            'games': reverse(GameList.name, request=request),
            'scores' : reverse(PlayerScoreList.name, request = request)
        })
