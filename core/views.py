from flask import Blueprint, render_template

from .models import Post

post = Blueprint("post", __name__, url_prefix='/')

posts = Post.query.all()

@post.route("/")
def home_page():
    return render_template(
        "index.html",
        posts_all=posts[:4],
        page_title="Accueil",
        subheading="Bienvenu(e) sur Clean Blog"
    )


@post.route("/blog")
def blog_page():
    return render_template(
        "pages/blog/list.html",
        posts_all=posts,
        page_title="Blog",
        subheading="Liste des articles"
    )


@post.route("/blog/<int:post_id>")
def blog_detail_page(post_id):

    article = Post.query.get_or_404(post_id)
    
    return render_template(
        "pages/blog/detail.html",
        post=article,
        page_title=article.post_title,
        subheading=article.post_subtitle
    )


@post.route("/contact/")
def contact_page():
	return render_template(
        "pages/contact.html",
        page_title="Contact",
        subheading="Laissez-nous un message"
    )


@post.route("/support/")
def support_page():
    return render_template(
        "pages/support.html",
        page_title="Support",
        subheading="Besoin d'aides ?"
    )
