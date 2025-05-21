from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from GameSession import game
from lobby import find_lobby

async def pole_keyboards():
    buttons = []
    for row in range(3): 
        line = []
        for col in range(3): 
            line.append(
                InlineKeyboardButton(
                    text=game.field[row][col], 
                    callback_data=f"{row}{col}{game.turn}"
                    )
                )
        buttons.append(line)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


keyboards_buttons = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text="🤼‍♂ Присоединиться к лобби")],[KeyboardButton(text="🕹 Играть")]],
    resize_keyboard=True,)

# async def lobby_keyboards():
#     buttons = []
#     for row in range(3): 
#         line = []
#         for col in range(3):          
#             line.append(InlineKeyboardButton(
#                 text=lb_game.game_session.field[row][col], 
#                 callback_data=f"{row}{col}{lb_game.game_session.turn}"))
#         buttons.append(line)
#     return InlineKeyboardMarkup(inline_keyboard=buttons)


async def lobby_keyboards(user_id):
    buttons = []
    for row in range(3): 
        line = []
        for col in range(3):
            lobby = find_lobby(user_id)
            line.append(InlineKeyboardButton(
                text=lobby.game_session.field[row][col], 
                callback_data=f"game_{row}{col}{lobby.game_session.turn}"))
        buttons.append(line)
    return InlineKeyboardMarkup(inline_keyboard=buttons)




# async def lobby_keyboards(current_user_id: int):
#     buttons = []
#     for row in range(3):
#         line = []
#         for col in range(3):
#             cell=lb_game.game_session.field[row][col]
#             if cell != " ":
#                 # Клетка занята — делаем неактивную кнопку
#                 text = cell
#                 callback = "ignore"
#             elif lb_game.game_session.current_player_id != current_user_id:
#                 # Не очередь этого игрока — отключаем кнопку
#                 text = " "
#                 callback = "ignore"
#             else:
#                 # Очередь игрока — активная кнопка
#                 text = game.turn
#                 callback = f"{row}{col}{game.turn}"
            
#             line.append(InlineKeyboardButton(text=text, callback_data=callback))
#         buttons.append(line)
    
#     return InlineKeyboardMarkup(inline_keyboard=buttons)