import time
from database.db import *
from datetime import datetime

def get_day_number():
    day_number = datetime.today().isoweekday() + 1
    day_aliya = "aliya" + str(day_number)
    return day_number

def get_day_name():
    day_name = datetime.today().strftime("%A")
    return day_name

def get_text_aliya():

    day = get_day_number()
    section = "section" + str(day)
    aliya = "aliya" + str(day)
    titleReflection = "titleReflection" + str(day)
    reflection = "reflection" + str(day)
    verso = "verso" + str(day)

    if aliya == "aliya8":
        aliya = "aliya1"
        section = "sect1"

    query = (
        "SELECT nroParasha, nameParasha, signParasha, "
        + section
        + ", "
        + aliya
        + ", "
        + titleReflection
        + ", "
        + reflection
        + ", "
        + verso
        + ", sectionHaftara, haftara FROM parasha WHERE isPublic = true"
    )

    print(query)
    connection_DB =connection.cursor()
    connection_DB.execute(query)
    data = connection_DB.fetchone()
    if data:
        data_list= list(data)
    else:
        data_list = ['Test','Test','Test','Test','Test','Test','Test','Test','Test','Test',]
    connection_DB.close()
    return data_list


def get_parashot_list():
    try:
        query = "SELECT nroParasha , nameParasha FROM parasha"
        connection_DB = connection.cursor()
        connection_DB.execute(query)
        data = connection_DB.fetchall()

        parashot_list = data

        parashot_objects = []
        for parasha_tuple in parashot_list:
            parashot_objects.append({"nro": parasha_tuple[0], "nombre": parasha_tuple[1]})

        connection_DB.close()
        return parashot_objects
    except sqlite3.Error as e:
        print("ERROR =>")
        print(f"QUERY FAIL: {e}")
