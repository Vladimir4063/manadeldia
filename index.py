import time
from flask import Flask, render_template
from database.db import *


app = Flask(__name__)

@app.route('/')
def home():

    connection_DB =connection.cursor()
    connection_DB.execute('SELECT nameParasha, aliya1 , aliya2  FROM parasha where nameParasha = "Bamidbar"')
    print("GET")

    data = connection_DB.fetchone()
    data_list= list(data)

    print(data_list[2])


    # data_list = list(data)

    # print(type(data_list[0]))

    # for data_l in data_list:
    #     print(data_l)
    time.sleep(3)


    return render_template('index.html', data_list = data_list)

if __name__ == '__main__':
    app.run()