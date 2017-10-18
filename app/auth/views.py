from flask import render_template, request, redirect, flash, url_for

from app.decorators import login_required
from app.utils import flash_errors, add_user, login_user, logout_user
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import auth
from app.models import Users, User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.filter_by(email=form.email.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
        return redirect(request.args.get('next') or url_for('main.get_recipes'))
    else:
        flash_errors(form)
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category="msg")
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = User(username=username, email=email)
            user.password=password
            add_user(user)
            flash('You can now login.', category="success")
            return redirect(url_for('auth.login'))
    else:
        flash_errors(form)

    return render_template('auth/register.html', form=form)
