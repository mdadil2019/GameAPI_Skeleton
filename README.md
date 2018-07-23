# GameAPI_Skeleton
An skeleton API of game using django rest framework and postgresQL


Player endpoint: http://127.0.0.1:8000/players/

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "url": "http://127.0.0.1:8000/players/1/",
        "name": "kevin",
        "gender": "M",
        "gender_description": "Male",
        "scores": [
            {
                "url": "http://127.0.0.1:8000/player-scores/2/",
                "pk": 2,
                "score": 25000,
                "score_date": "2016-06-21T03:02:00Z",
                "game": {
                    "url": "http://127.0.0.1:8000/games/2/",
                    "game_category": "3D RPG",
                    "name": "Superman vs Aquaman",
                    "released_date": "2016-06-21T03:02:00Z",
                    "played": false
                }
            },
            {
                "url": "http://127.0.0.1:8000/player-scores/3/",
                "pk": 3,
                "score": 19000,
                "score_date": "2016-09-21T03:02:00Z",
                "game": {
                    "url": "http://127.0.0.1:8000/games/1/",
                    "game_category": "3D RPG",
                    "name": "God of War",
                    "released_date": "2016-06-21T03:02:00Z",
                    "played": false
                }
            }
        ]
    },
    {
        "url": "http://127.0.0.1:8000/players/2/",
        "name": "Patric",
        "gender": "M",
        "gender_description": "Male",
        "scores": [
            {
                "url": "http://127.0.0.1:8000/player-scores/1/",
                "pk": 1,
                "score": 35000,
                "score_date": "2016-06-21T03:02:00Z",
                "game": {
                    "url": "http://127.0.0.1:8000/games/2/",
                    "game_category": "3D RPG",
                    "name": "Superman vs Aquaman",
                    "released_date": "2016-06-21T03:02:00Z",
                    "played": false
                }
            }
        ]
    }
]
```
