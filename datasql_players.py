import sqlite3

db = sqlite3.connect("data_sqlite.db")

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS stats (
          users_id integer,
          wins integer,
          losses integer
)""")

db.close()

def join(user_id):
    with sqlite3.connect("data_sqlite.db") as conn:
        c = conn.cursor()
        items = c.execute("SELECT users_id FROM stats")
        itemslist = list(items)
        if (user_id,) not in itemslist:
            c.execute("INSERT INTO stats VALUES(?,0,0)",(user_id,))
        conn.commit()

           
def win(user_id):
    with sqlite3.connect("data_sqlite.db") as conn:
        c = conn.cursor()
        c.execute("UPDATE stats SET wins = wins +1 WHERE users_id = ?",(user_id,))
        conn.commit()
                    

def losses(user_id):
    with sqlite3.connect("data_sqlite.db") as conn:
        c = conn.cursor()
        c.execute("UPDATE stats SET losses = losses +1 WHERE users_id = ?",(user_id,))
        conn.commit()



def parsing(user_id):
    with sqlite3.connect("data_sqlite.db") as conn:
        c = conn.cursor()
        wins = c.execute("SELECT wins FROM stats WHERE users_id = ?",(user_id,))
        losses = c.execute("SELECT losses FROM stats WHERE users_id = ?",(user_id,))
        conn.commit()
        return wins,losses
        
    
