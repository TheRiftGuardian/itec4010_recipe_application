# ITEC 4010 Recipe Application

## Setup:
Download files and open with your Python IDE.

if `requirements.txt` does not automatically download the required packages you an run the commands:
On Windows type: <br>
`python -m pip install -r requirements.txt`

On MacOS type: <br>
`pip3 install -r requirements.txt`

## General Info:
Flask sets up web applications by having all their html files in a directory called `templates`.
We can reference these html files by name without including file path and render the templates <br>
To render the file `index.html`: <br>
`return render_template("index.html")` <br>

`@app.route` functions indeciates routes one can navigate on the website. <br>
A route called '/logout' would be the url  <br>
`website_name.com/logout` <br>

Remember to also mention the methods a page will use when creating a new route. <br>
`@app.route("/post/<int:post_id>", methods=["GET", "POST"])` <br>
A page that displays the recipes details would require `GET` to obtain post data and `POST` to edit post data. <br>

Flask allows you to input code in html files using the syntax: <br>
`{% code_here %}` <br>
for loops, if statements, etc. cam be written here. <br>
When writing conditional statements and for loops you must indicate the end as well. <br>
EX: <br>
`{% endfor %}` <br>
`{% endif %}` <br>

To display object properties <br>
`{{object.attribute}}` <br>

Example: <br>
`{% for post in all_posts %}` <br>
` <h1> {{ post.title }} </h1>` <br>
 `<h2> {{ post.subtitle }} </h2>` <br>
`{% endfor %}` <br>
`<h3> Other text ...  </h3>` <br>
This exmaple iterates through all posts and creates two `<h1>` tags for each posts title and subtitle. <br>

Example two: <br>
`<a href="{{url_for('add_new_post')}}"> Create New Post </a>` <br>
Creates a button/link that will trigger a function called `add_new_post` which routes to: <br>
`websitename.com/new-post` <br>
and renders a new page. <br>

Flask can also "section" html pages so repetition isn't necessary when creating new pages. <br>
Having pages header.html and footer.html allows for pages like index.html to utlize code like: <br>
`{% include "header.html" %}` at the top <br>
and `{% include "footer.html" %}` at the bottom <br>
in their own html files which display the same universal header and footer. <br>
This is great when a change to the header is being made and you don't have to do it to each and every page with the same header. <br>

Forms can be render with the function `render_form` in an html file. They must take a FlaskForm object.  <br>
Creating new forms is simple: <br>
`class CreateRecipeForm(FlaskForm): <br>
    title = StringField("Recipe Post Title", validators=[DataRequired()]) <br>
    subtitle = StringField("Subtitle", validators=[DataRequired()]) <br>
    img_url = StringField("Recipe Image URL", validators=[DataRequired(), URL()]) <br>
    body = CKEditorField("Recipe Content", validators=[DataRequired()]) <br>
    submit = SubmitField("Submit Post")` <br>
^^^ <br>
This is an example.  <br>
There are multiple Fields and validators to choose from depending on application. Check WTFForms documentation for anything special. <br>
https://wtforms.readthedocs.io/en/3.2.x/fields/#basic-fields <br>

Notes: <br>
`DataRequired()` =  input must not be null <br>
`URL()` = input must be a URL <br>

You can take a peep at the database using an application called DB Browser for SQLite. <br>
![image](https://github.com/user-attachments/assets/ef9e3804-75aa-4ae7-bdc9-3440fff68826) <br>



## Documentations:

WTForms
https://wtforms.readthedocs.io/en/3.2.x/

Flask
https://flask.palletsprojects.com/en/stable/

SQLite3
https://docs.python.org/3/library/sqlite3.html

Werkzeug (Security)
https://werkzeug.palletsprojects.com/en/stable/



