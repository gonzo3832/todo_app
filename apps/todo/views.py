from re import I
from apps.app import db
from flask import Blueprint, render_template, redirect, url_for
from apps.todo.forms import ToDoForm
from apps.todo.models import ToDo
todo = Blueprint(
    'todo',
    __name__,
    template_folder='templates',
    static_folder='static'

)

@todo.route("/",methods = ['GET', 'POST'])
def index():
    form = ToDoForm()
    tasks = db.session.query(ToDo).all()

    if form.validate_on_submit(): #submitされた際に実行
        task = ToDo(
            todo = form.todo.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("todo.index"))    
    return render_template("todo/index.html",form=form,tasks = tasks)