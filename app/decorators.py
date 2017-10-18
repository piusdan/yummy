from functools import wraps
from flask import request, render_template, jsonify, g, flash, redirect, url_for

def handle_errors(code):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            message = f(*args, **kwargs)
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                response = jsonify({'error': message})
                response.status_code = code
                return response
            return render_template('errors/error.html', message=message, code=code), code
        return decorated_function
    return decorator

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.current_user is None:
            flash("login to access this view")
            redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function



