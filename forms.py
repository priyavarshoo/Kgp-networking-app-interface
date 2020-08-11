from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5 , max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4 , max=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    contact = StringField('Contact Number', validators=[DataRequired(),Length(min=10 , max=10)])
    year_study = StringField('Year Of Study', validators=[DataRequired(), Length(min=3, max=15)])
    department= StringField('Department',validators=[DataRequired(),Length(max=50)])
    hostel= StringField('Hall Of Residence/Hostel',validators=[DataRequired(),Length(max=80)])
    submit =SubmitField('Sign Up')
class AdminRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5 , max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4 , max=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    contact = StringField('Contact Number', validators=[DataRequired(),Length(min=10 , max=10)])
    organization = StringField('Name Of Organization', validators=[DataRequired(), Length(min=1, max=15)])
    description= StringField('Description',validators=[DataRequired(),Length(max=50)])
    submit =SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4 , max=8)])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Login')

