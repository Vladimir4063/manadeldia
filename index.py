import time
from flask import Flask, render_template, request
from database.db import *
from models.get_utils import get_day_number, get_parashot_list, get_text_aliya
from models.post_utils import post_text_parasha
from models.update_utils import update_parasha_public

app = Flask(__name__)


@app.route("/")
def home():
    data_list = get_text_aliya()
    nro_parasha = data_list[0]
    name_parasha = data_list[1]
    sign_parasha = data_list[2]
    sect_aliya = data_list[3]
    text_aliya = data_list[4]
    title_reflection = data_list[5]
    text_reflection = data_list[6]
    featured_verse = data_list[7]
    section_haftara = data_list[8]
    text_haftara = data_list[9]

    day = get_day_number()

    return render_template(
        "index.html",
        nro_parasha=nro_parasha,
        name_parasha=name_parasha,
        sign_parasha=sign_parasha,
        sect_aliya=sect_aliya,
        text_aliya=text_aliya,
        title_reflection=title_reflection,
        text_reflection=text_reflection,
        featured_verse=featured_verse,
        section_haftara=section_haftara,
        text_haftara=text_haftara,
        day=day,
    )


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":

        return render_template("admin.html")

    else:
        nroParasha = request.form["nroParasha"]
        nameParasha = request.form["nameParasha"]
        signParasha = request.form["signParasha"]

        section1 = request.form["section1"]
        aliya1 = request.form["aliya1"]
        verso1 = request.form["verso1"]
        titleReflection1 = request.form["titleReflection1"]
        reflection1 = request.form["reflection1"]

        section2 = request.form["section2"]
        aliya2 = request.form["aliya2"]
        verso2 = request.form["verso2"]
        titleReflection2 = request.form["titleReflection2"]
        reflection2 = request.form["reflection2"]

        section3 = request.form["section3"]
        aliya3 = request.form["aliya3"]
        verso3 = request.form["verso3"]
        titleReflection3 = request.form["titleReflection3"]
        reflection3 = request.form["reflection3"]

        section4 = request.form["section4"]
        aliya4 = request.form["aliya4"]
        verso4 = request.form["verso4"]
        titleReflection4 = request.form["titleReflection4"]
        reflection4 = request.form["reflection4"]

        section5 = request.form["section5"]
        aliya5 = request.form["aliya5"]
        verso5 = request.form["verso5"]
        titleReflection5 = request.form["titleReflection5"]
        reflection5 = request.form["reflection5"]

        section6 = request.form["section6"]
        aliya6 = request.form["aliya6"]
        verso6 = request.form["verso6"]
        titleReflection6 = request.form["titleReflection6"]
        reflection6 = request.form["reflection6"]

        section7 = request.form["section7"]
        aliya7 = request.form["aliya7"]
        verso7 = request.form["verso7"]
        titleReflection7 = request.form["titleReflection7"]
        reflection7 = request.form["reflection7"]

        sectionHaftara = request.form["sectionHaftara"]
        haftara = request.form["haftara"]

        post_text_parasha(
            nroParasha,
            nameParasha,
            signParasha,
            section1,
            aliya1,
            verso1,
            titleReflection1,
            reflection1,
            section2,
            aliya2,
            verso2,
            titleReflection2,
            reflection2,
            section3,
            aliya3,
            verso3,
            titleReflection3,
            reflection3,
            section4,
            aliya4,
            verso4,
            titleReflection4,
            reflection4,
            section5,
            aliya5,
            verso5,
            titleReflection5,
            reflection5,
            section6,
            aliya6,
            verso6,
            titleReflection6,
            reflection6,
            section7,
            aliya7,
            verso7,
            titleReflection7,
            reflection7,
            sectionHaftara,
            haftara,
        )
        return render_template("admin.html")


@app.route("/admin-push", methods=["GET", "POST"])
def admin_push():
    parashot_list = get_parashot_list()

    if request.method == "GET":
        return render_template("admin-push.html", parashot_list=parashot_list)
    else:
        nroParasha = request.form["nroParasha"]
        update_parasha_public(nroParasha)
        return render_template("admin-push.html", parashot_list=parashot_list)


if __name__ == "__main__":
    app.run(debug=True)
