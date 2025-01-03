from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, URL, NumberRange, Optional
from flask_ckeditor import CKEditorField

# Import Recipe Enumerator for additional recipe details
from Recipe_Enum import DietaryChoice, TimeSpent, MealTime, MealCost


# A form for creating a recipe post
class CreateRecipeForm(FlaskForm):
    title = StringField("Recipe Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Recipe Image URL", validators=[DataRequired(), URL()])

    dietary_choice = SelectField(
        "Dietary Choice",
        choices=[(choice.name, choice.value.replace("_", " ").title()) for choice in DietaryChoice],
        validators=[DataRequired()],
    )

    time_spent = SelectField(
        "Time Spent",
        choices=[(choice.name, choice.value) for choice in TimeSpent],
        validators=[DataRequired()],
    )

    meal_cost = SelectField(
        "Meal Cost",
        choices=[(choice.name, choice.value) for choice in MealCost],
        validators=[DataRequired()],
    )

    meal_time = SelectField(
        "Meal Time",
        choices=[(choice.name, choice.value.replace("_", " ").title()) for choice in MealTime],
        validators=[DataRequired()],
    )

    ingredients = CKEditorField("Recipe Ingredients", validators=[DataRequired()])
    instructions = CKEditorField("Recipe Instructions", validators=[DataRequired()])

    submit = SubmitField("Submit Post")


# A form to register new users
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# A form to login existing users
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In!")


# A form to add comments
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


# A form to filter recipes
class RecipeFilterForm(FlaskForm):
    dietary_choice = SelectField(
        'Dietary Choice',
        choices=[('', 'Any Dietary Choice')] + [(choice.value, choice.name.title().replace('_', ' ')) for choice in
                                                DietaryChoice],
        coerce=str
    )
    time_spent = SelectField(
        'Time Spent',
        choices=[('', 'Any Time Spent')] + [(choice.value, choice.name.title().replace('_', ' ')) for choice in
                                            TimeSpent],
        coerce=str
    )
    meal_cost = SelectField(
        'Meal Cost',
        choices=[('', 'Any Meal Cost')] + [(choice.value, choice.name.title().replace('_', ' ')) for choice in
                                           MealCost],
        coerce=str
    )
    meal_time = SelectField(
        'Meal Time',
        choices=[('', 'Any Meal Time')] + [(choice.value, choice.name.title()) for choice in MealTime],
        coerce=str
    )
    submit = SubmitField('Filter')
