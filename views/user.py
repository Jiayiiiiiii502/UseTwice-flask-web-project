from flask import Blueprint, render_template

bp = Blueprint("user", __name__, url_prefix='/user')


@bp.route("/registrate", methods=['GET', 'POST'])
def registrate():
    return render_template("user_regirstrate.html")

@bp.route("/login")
def login():
    return render_template("user_login.html")


