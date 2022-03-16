from flask import Blueprint, render_template

todo = Blueprint(
    'todo',
    __name__,
    template_folder='templates',
    static_folder='static'

)

@todo.route("/")
def index():
    return render_template("todo/index.html")