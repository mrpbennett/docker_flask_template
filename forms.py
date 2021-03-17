from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email Address", "type": "email"},
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password", "type": "password"},
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class SignUpForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=2, max=20)],
        render_kw={"placeholder": "Username"},
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email Addresss"},
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "***"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "***"},
    )
    submit = SubmitField("Sign Up")
