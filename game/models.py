from django.db import models

# Create your models here.
# We will be performing different crud operations on diffrent related resources
# Some of them are Game Categories, Games, Players, Player Score

class GameCategory(models.Model):
    name = models.CharField(max_length=200)

    # Ordering of the objects in database will be accroding to the name field
    class Meta:
        ordering = ('name',)

    # When we convert the GameCategory object into string then it will show the name column
    def __str__(self):
        return self.name


class Game(models.Model):
    #the date on which the game is inserted in database
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=144)

    #Foreign key to GameCategory
    #CASCADE deletion will delete all the games related to game category when we delete any Game Category
    game_category = models.ForeignKey(GameCategory,related_name='games',on_delete=models.CASCADE)

    #the date when game has been released
    released_date = models.DateTimeField()


    #indicate if the game is played by the player at least one or not
    played = models.BooleanField(default=False)

    # Ordering of the Game will be according to the name field
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name




class Player(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = ((MALE,'Male'), (FEMALE, 'Female'),)
    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=144)

    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


#Model to represt the score achived by the Player
class PlayerScore(models.Model):
    #Relation with players
    player = models.ForeignKey(Player, related_name='scores',on_delete=models.CASCADE)

    #Relations with games
    game = models.ForeignKey(Game,on_delete=models.CASCADE)

    #Game Foreign key
    score = models.IntegerField()

    #date and time in which the score was achived by the player
    score_date = models.DateTimeField()

    class Meta:
        #ordering of database in descending order of Scores
        ordering = ('-score',)
