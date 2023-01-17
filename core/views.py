from flask import Blueprint, render_template

from .models import Post

post = Blueprint("post", __name__, url_prefix='/')


@post.route("/")
def home_page():
    
    posts = Post.query.all()[:4]

    return render_template(
        "index.html",
        posts_all=posts,
        page_title="Page d'accueil"
    )


@post.route("/contact/")
def contact_page():

	return render_template(
        "pages/contact.html",
        page_title="Contact page"
    )


@post.route("/support/")
def support_page():
    return render_template(
        "pages/support.html",
        page_title="Support page"
    )
