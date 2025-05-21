import GameSession as gm

class Lobby:
    def __init__(self):
        self.player_x = None
        self.player_y = None
        self.game_session = gm.GameSession()

waiting_lobby = None


playing_lobbies = []

def handle_join(user_id):
    global waiting_lobby
    if waiting_lobby is None:
        waiting_lobby = Lobby()
        waiting_lobby.player_x = user_id
    else:
        waiting_lobby.player_y = user_id
        playing_lobbies.append(waiting_lobby)
        waiting_lobby = None

def find_lobby(user_id):
    for lobby in playing_lobbies:
        if user_id in [lobby.player_x,lobby.player_y]:
            return lobby

