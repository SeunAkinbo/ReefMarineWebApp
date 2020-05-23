from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, regexp

CHOICES = ['Oil & Gas', 'Shipping', 'Contractor']


class RegistrationForm(FlaskForm):
    company_name = StringField('Username', validators=[
                               DataRequired(), Length(min=2, max=20)])
    rc_num = StringField('Company Registration Number', validators=[
                         DataRequired(), Length(min=5, max=10)])
    category = SelectField('Category', validators=[
                           DataRequired()], choices=CHOICES)
    email = StringField('Email', validators=[DataRequired(), Email()])
    # image = FileField('Image File', validators=[regexp(u'^[^/\\]\.jpg$')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    register = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('login')
