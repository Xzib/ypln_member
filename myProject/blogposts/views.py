from flask import Blueprint,redirect,render_template,url_for
from myProject import db, mail
from myProject.models import RegisteredMember, BlogPost
from myProject.blogposts.forms import BlogPostForm
from flask import render_template,redirect,request,url_for,flash,abort
from flask_login import login_user, login_required,logout_user, current_user
from flask import Flask


blog_post_bp = Blueprint('blog_post_bp',__name__,
                                template_folder='templates/blogposts')


@blog_post_bp.route('/create')
@login_required
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title = form.title.data,
                                text = form.text.data,
                                user_id = current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog post successfully created')
        return redirect(url_for('member_login.profile'))
    return render_template('create_post.html', form=form)

@blog_post_bp.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html', title = post.title, date = post.date, post = post)
 

@blog_post_bp.route('/<int:blog_post_id>/update', methods = ['GET','POST'])
@login_required
def update(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    if post.author != current_user:
        abort(403)
    form = BlogPostForm()
    if form.validate_on_submit:
        post.title = form.title.data,
        post.text = form.text.data,
        db.session.commit()
        flash('Blog post successfully updated')
        return redirect(url_for('.blog_post',blog_post_id=blog_post_id))
    elif request.method=='GET':
        form.title.data = post.title
        form.text.data = post.text
    return render_template('create_post.html', title = 'Updating', form=form)


@blog_post_bp.route('/<int:blog_post_id>/delete', methods = ['GET','POST'])
@login_required
def delete(blog_post_id):
    post = BlogPost.query.get_or_404(blog_post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Blog Post deleted")
    return redirect(url_for('member_login.dashboard'))


# @member_profiles_bp.route('/list')
# @login_required
# def list_register_members():
#     members = RegisteredMember.query.all()
#     return render_template("thankyou.html", members=members)


# @member_profiles_bp.route('/thankyou')
# @login_required
# def thankyou():
#     return render_template("thankyou.html")