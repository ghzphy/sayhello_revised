from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

### 表单类: name, body
### 参考: https://blog.csdn.net/zyself/article/details/87828972
class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1,20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1,200)])
    submit = SubmitField()
