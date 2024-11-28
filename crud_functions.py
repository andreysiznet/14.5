import sqlite3


def initiate_db():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT
    )
    ''')
    connection.commit()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    cursor.execute('''
    SELECT * FROM Products
    ''')
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products


def add_user(username, email, age):
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('products_db.db')
    cursor = connection.cursor()
    user = cursor.execute("SELECT username FROM Users WHERE username = ?",
                          (username,)).fetchone()
    connection.commit()
    connection.close()
    if not user:
        return False
    else:
        return True