from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

# 从flask_wtf导入FlaskForm类
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    # DataRequired（） 方法检查字段是否为空
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
