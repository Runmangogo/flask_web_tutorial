from flask import Blueprint, render_template

# Blueprint it means this file has lots of rules inside, lots of urls defined.
# 同时可以让 views seperate 到不同的 files
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

