from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class ToDoForm(FlaskForm):
    todo = StringField(
        'やること',
        validators=[
            DataRequired(message="なんか書けや！！！"),
            length(max = 50, message = '長すぎや、５０字以内や')
        ]
    )
    submit = SubmitField("追加！！")