import sqlite3


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
    sql.execute("SELECT title, size, description, contacts, image FROM ads_clothes WHERE size = (?)", (size,))
    data = sql.fetchall()
    db.close()
    return data


def show_ads_shoes(size):
    db = sqlite3.connect('database/ads.db')
    sql = db.cursor()
    sql.execute("SELECT title, size, description, contacts, image FROM ads_shoes WHERE size = (?)", (size,))
    data = sql.fetchall()
    db.close()
    return data


def get_user_data(user_id):
    db = sqlite3.connect('database/users.db')
    sql = db.cursor()
    sql.execute("SELECT type, size FROM users WHERE user_id = (?)", (user_id,))
    data = sql.fetchone()
    db.close()
    return data
