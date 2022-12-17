import sqlite3
import json


def user(user_id):
    db = sqlite3.connect('database/users.db')
    sql = db.cursor()
    sql.execute("SELECT user_id FROM users WHERE user_id = (?)", (user_id,))
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, 0, ""))
        db.commit()
        db.close()
        return True
    else:
        db.close()
        return False


def update_type(typer, user_id):
    db = sqlite3.connect('database/users.db')
    sql = db.cursor()
    sql.execute("UPDATE users SET type = (?) WHERE user_id = (?)", (typer, user_id))
    db.commit()
    db.close()


def update_size(size, user_id):
    db = sqlite3.connect('database/users.db')
    sql = db.cursor()
    sql.execute("UPDATE users SET size = (?) WHERE user_id = (?)", (size, user_id))
    db.commit()
    db.close()


def is_admin(user_id):
    db = sqlite3.connect('database/admins.db')
    sql = db.cursor()
    sql.execute("SELECT admin_id FROM admins WHERE admin_id = (?)", (user_id,))
    if sql.fetchone() is None:
        db.close()
        return False
    else:
        db.close()
        return True


def new_clothes(title, size, description, contacts, image):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    sql.execute("INSERT INTO ads_clothes VALUES (?, ?, ?, ?, ?)", (title, size, description, contacts, image))
    db.commit()
    db.close()


def new_shoes(title, size, description, contacts, image):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    sql.execute("INSERT INTO ads_shoes VALUES (?, ?, ?, ?, ?)", (title, size, description, contacts, image))
    db.commit()
    db.close()


def show_ads_clothes(size):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    sql.execute("SELECT title, size, description, contacts, image FROM ads_clothes")
    data = sql.fetchall()
    new_data = []
    for i in data:
        size1 = i[1]
        size1 = size1.split(",")
        if size in size1:
            new_data.append(i)

    db.close()
    return new_data


def show_ads_shoes(size):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    sql.execute("SELECT title, size, description, contacts, image FROM ads_shoes")
    data = sql.fetchall()
    new_data = []
    for i in data:
        size1 = i[1]
        size1 = size1.split(",")
        if str(size) in size1:
            new_data.append(i)
    db.close()
    print(new_data)
    return new_data


def get_user_data(user_id):
    db = sqlite3.connect('database/users.db')
    sql = db.cursor()
    sql.execute("SELECT type, size FROM users WHERE user_id = (?)", (user_id,))
    data = sql.fetchone()
    db.close()
    return data


def delete_ad(title):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    if title[1] == "одежда":
        sql.execute("DELETE FROM ads_clothes WHERE title = (?)", (title[0],))
        print("ok")
    else:
        sql.execute("DELETE FROM ads_shoes WHERE title = (?)", (title[0],))
    db.commit()
    db.close()


def edit_ad(title, size):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    title = title.split("|")
    if title[1] == "одежда":
        sql.execute("UPDATE ads_clothes SET size = (?) WHERE title = (?)", (size, title[0]))
        print("ok")
    else:
        sql.execute("UPDATE ads_shoes SET size = (?) WHERE title = (?)", (size, title[0]))
    db.commit()
    db.close()
