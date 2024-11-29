from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey, Enum as SQLAlchemyEnum
from flask_login import UserMixin

from Recipe_Enum import DietaryChoice, TimeSpent, MealTime, MealCost


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# CONFIGURE TABLES
class RecipePost(Base):
    __tablename__ = "recipe_posts"
    # Recipe Post ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    # Reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="recipes")

    title: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)

    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    instructions: Mapped[str] = mapped_column(Text, nullable=False)

    # Dietary Choice
    # Low Carb, High Protein, Plant-Based, Dairy-free, Everything
    dietary_choice: Mapped[DietaryChoice] = mapped_column(SQLAlchemyEnum(DietaryChoice), nullable=False)

    # Time-spent cooking
    # Quick Bites (0–15 minutes), Simple Meals (15–30 minutes), . Balanced Dinners (30–45 minutes),
    # Meal Prep Sessions (45 minutes–1 hour), Special Occasion Meals (1 hour +)
    time_spent: Mapped[TimeSpent] = mapped_column(SQLAlchemyEnum(TimeSpent), nullable=False)

    # Estimated Meal cost Super Budget-Friendly ($0–$5 per serving), Affordable Eats ($5–$10 per serving),
    # Moderate Cost ($10–$15 per serving), Splurge Meals ($15+ per serving)
    meal_cost: Mapped[MealCost] = mapped_column(SQLAlchemyEnum(MealCost), nullable=False)

    # Mealtime
    # Breakfast, Lunch, Dinner, Snack
    meal_time: Mapped[MealTime] = mapped_column(SQLAlchemyEnum(MealTime), nullable=False)

    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Parent relationship to the comments
    comments = relationship("Comment", back_populates="parent_post",
                            cascade="all, delete-orphan",
                            )

    # Calculates the average rating for the current recipe post
    @property
    def average_rating(self):
        # If there are no comments/reviews, return None or 0
        if not self.comments:
            return None, 0

        total_rating = 0
        count = 0

        # Loop through each comment and get total ratings
        for comment in self.comments:
            # Handling potential errors that could somehow slip through

            if comment.star_rating is not None:
                total_rating += comment.star_rating
                count += 1

        if count == 0:
            return None

        # Calculate and return the average rating and number of reviews in tuple
        average_rating = round(total_rating / count, 1)

        return (average_rating, count)


# User table for all your registered users
class User(UserMixin, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    email: Mapped[str] = mapped_column(String(100), unique=True)

    password: Mapped[str] = mapped_column(String(100))

    name: Mapped[str] = mapped_column(String(100))

    # This will act like a list of RecipePost objects attached to each User.
    # The "author" refers to the author property in the RecipePost class.
    recipes = relationship("RecipePost", back_populates="author")

    # Parent relationship: "comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")


# Comment table for the comments on the recipe posts
class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    star_rating: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)

    # Child relationship:"users.id" The users refers to the tablename of the User class.
    # "comments" refers to the comments property in the User class.
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    # Child Relationship to the RecipePosts
    post_id: Mapped[str] = mapped_column(Integer, ForeignKey("recipe_posts.id"))
    parent_post = relationship("RecipePost", back_populates="comments")
