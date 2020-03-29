import sqlite3 as sqlite


connection = sqlite.connect('pizza.db')
connection.row_factory = sqlite.Row  # Enables accessing columns via names
database = connection.cursor()

def getLogin(username,password):
    result = database.execute("select * from musteri where username = ? and password = ?",(username,password)).fetchall()
    if(len(result) == 1):
        return result[0]
    return False

def musteriekle(name,surname,username,password):
     try:
         database.execute("insert into musteri values(?,?,?,?)",(name,surname,username,password));
         connection.commit()
         return True
     except:
         return False


def adminLogin(username, password):
    result = database.execute("select * from admin where username = ? and password = ?",(username,password)).fetchall()
    if(len(result) == 1):
        return result[0]
    return False


def adminekle(name, surname, username, password):
    try:
        database.execute("insert into admin values(?,?,?,?)", (name, surname, username, password));
        connection.commit()
        return True
    except:
        return False

def ekle(name, cost):
    try:
        database.execute("insert into list values(?,?)", (name, cost));
        connection.commit()
        return True
    except:
        return False


# def getContestant(id):
#     query = DBQueries.getContestant % id
#     result = database.execute(query).fetchone()
#     if result:
#         return dict(result)
#     return False
#
# def getNamesOfAllContestants():
#     result = database.execute(DBQueries.getNamesOfAllContestants).fetchall()
#     names = []
#     for name in result:
#         names.append(name[0])
#     return names
#
# # Sqlite is crazy ; allows strings for Integer. Fix on UI


 #connection.close()