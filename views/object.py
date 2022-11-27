from flask import Blueprint, render_template

bp=Blueprint("object",__name__,url_prefix='/object')

@bp.route('/')
def index():  # put application's code here
    return render_template("index.html")

@bp.route("/shopping_center")
def shop():
    return render_template("shop.html")

@bp.route("/detail")
def detail():
    return render_template("detail.html")

@bp.route("/like")
def like():
    return render_template("like.html")

@bp.route("/purchase_record")
def purchase_record():
    return render_template("purchase_record.html")

@bp.route("/sell")
def sell():
    return render_template("sell.html")

@bp.route("/my_sell")
def my_sell():
    return render_template("my_sell.html")



