from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory
from .models import * 
from . import db
import mimetypes

views = Blueprint('views', __name__)

mimetypes.add_type('application/javascript', '.js')

@views.after_request
def set_headers(response):
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/resume', methods=['GET', 'POST'])
def resume():
    return render_template("resume.html")

@views.route('/game', methods=['GET', 'POST'])
def game():
    return render_template("game.html")

@views.route('/donate', methods=['GET', 'POST'])
def donate():
    return render_template("donate.html")

@views.route('/display', methods=['GET', 'POST'])
def display():
   return send_from_directory("static/game", "test.html")

@views.route('/<path:path>')
def static_files(path):
    print("Attempting access to " + path)
    return send_from_directory('static/game', path)

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