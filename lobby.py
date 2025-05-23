import GameSession as gm

class Lobby:
    def __init__(self,player_x):
        self.player_x = player_x
        self.player_y = None
        self.player_x_message = None
        self.player_y_message = None
        self.game_session = gm.GameSession()
        self.player_turn = self.player_x
           

    def switch_player_turn(self):
        self.player_turn = self.player_x if self.player_turn == self.player_y else self.player_y



waiting_lobby = None


playing_lobbies = []

def handle_join(user_id):
    global waiting_lobby
    if waiting_lobby is None:
        waiting_lobby = Lobby(user_id)
    else:
        waiting_lobby.player_y = user_id
        playing_lobbies.append(waiting_lobby)
        waiting_lobby = None

def find_lobby(user_id):
    for lobby in playing_lobbies:
        if user_id in [lobby.player_x,lobby.player_y]:
            return lobby

