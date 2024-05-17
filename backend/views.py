from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from .models import * 
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/resume', methods=['GET', 'POST'])
def resume():
    return render_template("resume.html")

@views.route('/comment', methods=['GET', 'POST'])
def comment():
    data = request.form
    print(data)
    posts = Comment.query.order_by(Comment.date.desc())

    if request.method == "POST":
        author = request.form.get("author")
        content = request.form.get("content")
        if author == '':
            author = "Anonymous"

        newComment : Comment
        newComment = Comment(author=author, content=content)
        db.session.add(newComment)
        db.session.commit()

    return render_template("comments.html", query=posts)