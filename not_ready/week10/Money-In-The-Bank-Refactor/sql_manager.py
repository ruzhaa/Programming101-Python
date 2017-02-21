import sqlite3
import random
import hashlib
from client import Client


conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
                      clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT,
                      salt TEXT,
                      balance REAL DEFAULT 0,
                      message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = '''UPDATE clients
                    SET message = ?
                    WHERE id = ?'''

    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = '''UPDATE clients
                    SET password = ?
                    WHERE id = ?'''

    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def generate_salt():
    rbits = random.getrandbits(256)
    m = hashlib.sha256()
    m.update(str(rbits).encode('utf-8'))
    return m.hexdigest()


def hash_my_password(password, salt=None):
    m = hashlib.sha256()
    if salt is None:
        salt = generate_salt()

    pass_and_salt = password + salt
    m.update(pass_and_salt.encode('utf-8'))
    return (m.hexdigest(), salt)


def register(username, password):
    insert_sql = '''INSERT into clients (username, password, salt)
                    VALUES (?, ?, ?)'''
    password, salt = hash_my_password(password, salt=None)
    cursor.execute(insert_sql, (username, password, salt))
    conn.commit()


def get_salt(username):
    select_salt_by_username = '''SELECT salt
                                 FROM clients
                                 WHERE username = ?
                                 LIMIT 1'''
    cursor.execute(select_salt_by_username, (username,))
    my_salt = cursor.fetchone()
    return my_salt[0]


def login(username, password):
    select_query = '''SELECT id, username, balance, message
                      FROM clients
                      WHERE username = ? AND password = ?
                      LIMIT 1'''
    salt = get_salt(username)

    hash_password, _ = hash_my_password(password, salt=salt)
    cursor.execute(select_query, (username, hash_password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
