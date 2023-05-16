import sqlite3

try:
    connection = sqlite3.connect("database/database.sqlite", check_same_thread=False)
except Exception as error:
    print(error)