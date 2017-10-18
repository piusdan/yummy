from flask import flash, g

from app.models import Users


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), category="errors")


def add_user(user):
    Users.add(user)
    return True


def login_user(user):
    g.current_user = user


def logout_user():
    g.current_user = None