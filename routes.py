from flask import Blueprint
from datetime import date
from flask import abort, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import select, and_

# Imported forms from the forms.py
from forms import CreateRecipeForm, RegisterForm, LoginForm, CommentForm, RecipeFilterForm

# Imported models and recipe enumerators from the models.py
from models import RecipePost, User, Comment, DietaryChoice, TimeSpent, MealTime, MealCost

# Imported db from the db.py
from db import db

# Flask Blueprint for the main.py to utilize routes
route_controller = Blueprint('route_controller', __name__, template_folder="templates")


# A route decorator for admin and authors
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if f.__name__ == 'delete_post':
            post_id = kwargs.get('post_id')
            requested_post = db.get_or_404(RecipePost, post_id)
            if current_user.id != 1 and current_user.id != requested_post.author_id:
                return abort(403)
        # Otherwise continue with the route function
        elif f.__name__ == 'add_new_post':
            if not current_user.is_authenticated:
                return abort(403)
        elif f.__name__ == 'delete_comment':
            comment_id = kwargs.get('comment_id')
            requested_comment = db.get_or_404(Comment, comment_id)
            if current_user.id != 1 and current_user.id != requested_comment.author_id:
                return abort(403)
        # Any other admin related route will abort if id is not 1.
        elif current_user != 1:
            return abort(403)
        return f(*args, **kwargs)

    return decorated_function


# Register new users into the User database
@route_controller.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():

        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('route_controller.login'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # This line will authenticate the user with Flask-Login
        # Immediately logging them in after registration
        login_user(new_user)
        return redirect(url_for("route_controller.get_all_posts"))
    return render_template("register.html", form=form, current_user=current_user)


@route_controller.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()

        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('route_controller.login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('route_controller.login'))
        else:
            login_user(user)
            return redirect(url_for('route_controller.get_all_posts'))

    return render_template("login.html", form=form, current_user=current_user)


@route_controller.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('route_controller.get_all_posts'))


# Function to filter recipes based on form input
def filter_recipes_using_execute(db, dietary_choice=None, time_spent=None, meal_cost=None, meal_time=None):
    query = select(RecipePost)

    # Collect filter conditions list
    filters = []

    if dietary_choice:
        filters.append(RecipePost.dietary_choice == dietary_choice)

    if time_spent:
        filters.append(RecipePost.time_spent == time_spent)

    if meal_cost:
        filters.append(RecipePost.meal_cost == meal_cost)

    if meal_time:
        filters.append(RecipePost.meal_time == meal_time)

    # Apply all filters if any
    if filters:
        query = query.where(and_(*filters))

    # Execute the query
    result = db.session.execute(query).scalars().all()

    return result


@route_controller.route('/', methods=['GET', 'POST'])
def get_all_posts():
    form = RecipeFilterForm()

    # Default filter if no form submitted
    dietary_choice = None
    time_spent = None
    meal_cost = None
    meal_time = None

    if form.validate_on_submit():
        # Get filter values from the form and convert strings to enum values
        dietary_choice = DietaryChoice(form.dietary_choice.data) if form.dietary_choice.data != '' else None
        time_spent = TimeSpent(form.time_spent.data) if form.time_spent.data != '' else None
        meal_cost = MealCost(form.meal_cost.data) if form.meal_cost.data != '' else None
        meal_time = MealTime(form.meal_time.data) if form.meal_time.data != '' else None

    # Use the filter recipe function to filter recipes based on form selections
    posts = filter_recipes_using_execute(
        db,
        dietary_choice=dietary_choice,
        time_spent=time_spent,
        meal_cost=meal_cost,
        meal_time=meal_time
    )

    # Calculate average ratings for the posts
    for post in posts:
        post.avg_rating = post.average_rating

    return render_template("index.html", all_posts=posts, current_user=current_user, form=form)


@route_controller.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(RecipePost, post_id)

    comment_form = CommentForm()

    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("route_controller.login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            star_rating=comment_form.star_rating.data,
            comment_author=current_user,
            parent_post=requested_post,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_comment)
        db.session.commit()

        # Clear Comment Fields
        comment_form.comment_text.data = ""
        comment_form.star_rating.data = None

    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


# Use a decorator so only admin and logged in users can add new posts.
@route_controller.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreateRecipeForm()
    if form.validate_on_submit():
        new_post = RecipePost(
            title=form.title.data,
            subtitle=form.subtitle.data,

            ingredients=form.ingredients.data,
            instructions=form.instructions.data,

            dietary_choice=form.dietary_choice.data,
            time_spent=form.time_spent.data,
            meal_cost=form.meal_cost.data,
            meal_time=form.meal_time.data,

            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("route_controller.get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# Only an admin user or the author can edit a recipe post
@route_controller.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(RecipePost, post_id)
    edit_form = CreateRecipeForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,

        ingredients=post.ingredients,
        instructions=post.instructions
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user

        post.ingredients = edit_form.ingredients.data
        post.instructions = edit_form.instructions.data

        db.session.commit()
        return redirect(url_for("route_controller.show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


# Only an admin user or the author can delete a recipe post
@route_controller.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(RecipePost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('route_controller.get_all_posts'))


# Only an admin user or the author can delete a comment
@route_controller.route("/delete_comment/<int:comment_id>")
@admin_only
def delete_comment(comment_id):
    comment_to_delete = db.get_or_404(Comment, comment_id)
    print(comment_to_delete)
    print('comment deleted!')
    post_id = comment_to_delete.post_id
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for('route_controller.show_post', post_id=post_id))



# Simple about route that shows group members of assignment
@route_controller.route("/about")
def about():
    return render_template("about.html", current_user=current_user)
