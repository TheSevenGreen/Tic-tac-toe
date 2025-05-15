import keyboards as kb
import GameSession as gm

class Lobby:
    def __init__(self):
        self.player_x = None
        self.player_y = None
        self.game_session = gm.GameSession()
        test = self.game_session

waiting_lobby = None

d = 1
d2 = 2

playing_lobbies = {
    f"lobby{d}":{"player_x":24323423, "player_y": 24323443},
    f"lobby{d2}":{"player_x":243233, "player_y": 243443}
}

def handle_join(user_id):
    global waiting_lobby
    if waiting_lobby is None:
        waiting_lobby = Lobby()
        waiting_lobby.player_x = user_id
    else:
        waiting_lobby.player_y = user_id
        playing_lobbies.append(waiting_lobby)
        waiting_lobby = None

game = Lobby()

print(game.self.game_session.self.field)