import time
from flask import Flask, render_template
from database.db import *
from models.get_aliya import get_text_aliya

app = Flask(__name__)

@app.route("/")
def home():
    data_list = get_text_aliya()

    nro_parasha = data_list[0]
    name_parasha = data_list[1]
    sign_parasha = data_list[2]
    sect_aliya = data_list[3]
    text_aliya = data_list[4]

    return render_template(
        "index.html", 
        nro_parasha = nro_parasha,
        name_parasha = name_parasha,
        sign_parasha = sign_parasha,
        sect_aliya = sect_aliya,
        text_aliya = text_aliya
    )

if __name__ == "__main__":
    app.run(debug=True)
