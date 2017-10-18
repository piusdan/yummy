# -*- coding: utf-8 -*-

from flask import render_template
from app.main import main

@main.route('/')
def index():
    return render_template('auth/splash.html')

@main.route('/recipe')
def get_recipes():
    return render_template('main/main.html')

@main.route('/recipe/<int:id>')
def get_recipe():
    return True

@main.route('/delete-recipe/<int:id>')
def delete_recipe(id):
    return True

@main.route('/add-recipe', methods=['POST'])
def add_recipe():
    return True

@main.route('/edit-recipe/<int:id>', methods=['POST'])
def edit_recipe(id):
    return True

@main.route('/create-recipe', methods=['POST'])
def create_recipe():
    return True