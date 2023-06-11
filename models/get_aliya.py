import time
from models.get_day import get_day_number
from database.db import *

def get_text_aliya():

    day = get_day_number()
    sect = "sect" + str(day)
    aliya = "aliya" + str(day)

    if aliya == "aliya8":
        aliya = "aliya1"
        sect = "sect1"

    query = "SELECT nroParasha, nameParasha, signParasha, " + sect +", " + aliya +" FROM parasha WHERE id = id"
    connection_DB =connection.cursor()
    connection_DB.execute(query)
    data = connection_DB.fetchone()
    data_list= list(data)
    return data_list
