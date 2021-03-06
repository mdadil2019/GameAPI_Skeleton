from rest_framework import serializers
from game.models import Game,GameCategory,Player,PlayerScore

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    # Inside of Game Model we have created game_category field with related_name
    # as games that's why we have specified here the name games
    # The view_name is the name of the view that has to be called when use click on the hyperlink
    games = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'game-detail')

        # Fields that we want to serialize of GameCategory object
    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'game_category',
            'name',
            'released_date',
            'played'
        )

class ScoreSerializer(serializers.HyperlinkedModelSerializer):

    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game'
        )

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Player.GENDER_CHOICES
    )
    gender_description = serializers.CharField(
        source = 'get_gender_display',
        read_only=True
    )

    class Meta:
        model = Player
        fields = ('url','name','gender','gender_description','scores')

class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),slug_field='name')

    game = serializers.SlugRelatedField(queryset=Game.objects.all(),slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game'
        )
