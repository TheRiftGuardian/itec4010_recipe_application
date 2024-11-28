from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, NumberRange, Optional
from flask_ckeditor import CKEditorField


# WTForm for creating a recipe post
from Recipe_Enum import DietaryChoice, TimeSpent, MealTime, MealCost


class CreateRecipeForm(FlaskForm):
    title = StringField("Recipe Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Recipe Image URL", validators=[DataRequired(), URL()])

    #body = CKEditorField("Recipe Content", validators=[DataRequired()])
    ingredients = CKEditorField("Recipe Ingredients", validators=[DataRequired()])
    instructions = CKEditorField("Recipe Instructions", validators=[DataRequired()])

    # Dropdown Fields for recipe additional details
    dietary_choice = SelectField(
        "Dietary Choice",
        choices=[(choice.name, choice.value.replace("_", " ").title()) for choice in DietaryChoice],
        validators=[DataRequired()],
    )

    # Time spent on cooking with the descriptive range
    time_spent = SelectField(
        "Time Spent",
        choices=[(choice.name, choice.value) for choice in TimeSpent],
        validators=[DataRequired()],
    )

    # Meal cost field with the descriptive cost range
    meal_cost = SelectField(
        "Meal Cost",
        choices=[(choice.name, choice.value) for choice in MealCost],
        validators=[DataRequired()],
    )

    # Meal time
    meal_time = SelectField(
        "Meal Time",
        choices=[(choice.name, choice.value.replace("_", " ").title()) for choice in MealTime],
        validators=[DataRequired()],
    )


    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    star_rating = IntegerField("Star Rating (1-5)", validators=[DataRequired(), NumberRange(min=1, max=5)])
    star_rating = SelectField("Star Rating (1-5)", choices=
                              [('1', '★☆☆☆☆'),  # 1 star
        ('2', ' ★★☆☆☆'),  # 2 stars
        ('3', '★★★☆☆'),  # 3 stars
        ('4', '★★★★☆'),  # 4 stars
        ('5', '★★★★★')], coerce=int)
    comment_text = CKEditorField("Your Feedback (Optional)", validators=[Optional()])
    submit = SubmitField("Submit Comment")
