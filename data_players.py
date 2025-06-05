import json

def join_json(user_id):
    user_key = str(user_id)

    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    if user_key not in data:
        data[user_key] = {"wins": 0, "losses": 0}

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



def win_json(user_id):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        data[str(user_id)]["wins"] +=1

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def losses_json(user_id2):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        data[str(user_id2)]["losses"] +=1

    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def parsing_json(user_id):
     with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
     str_user_id = str(user_id)
     if str_user_id in data:
         wins = data[str_user_id]["wins"]
         losses = data[str_user_id]["losses"]
         return wins,losses
  