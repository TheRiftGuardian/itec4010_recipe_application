from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_login import UserMixin

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

# CONFIGURE TABLES
class RecipePost(Base):
    __tablename__ = "recipe_posts"
    # Recipe Post ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    # Create reference to the User object. The "posts" refers to the posts property in the User class.
    author = relationship("User", back_populates="recipes")
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)

    #body: Mapped[str] = mapped_column(Text, nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    instructions: Mapped[str] = mapped_column(Text, nullable=False)

    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    # Parent relationship to the comments
    comments = relationship("Comment", back_populates="parent_post",
                            cascade="all, delete-orphan",
                            )

    @property
    def average_rating(self):
        # Calculate the average rating for the current recipe post
        if not self.comments:  # If there are no comments, return None or 0
            return None, 0

        total_rating = 0
        count = 0

        # Loop through each comment and accumulate the ratings
        for comment in self.comments:
            if comment.star_rating is not None:  # Make sure the comment has a star rating
                total_rating += comment.star_rating
                count += 1

        if count == 0:  # Avoid division by zero
            return None

        # Calculate and return the average rating and number of reviews in tuple
        average_rating = round(total_rating/ count, 1)

        return (average_rating, count)

# Create a User table for all your registered users
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


# Create a table for the comments on the recipe posts
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