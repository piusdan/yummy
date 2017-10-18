from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort


class Query(dict):
    """A dictionary on steroids - Hapa kazi tu
    """
    def set_cursor(self):
        """Tracks the number of items in the collection
        """
        self._cursor = max(self.keys())

    def get_cursor(self):
        """Get current largest item in the collection
        :returns the number of items in the collection
        """
        self.set_cursor()
        return self._cursor

    def first_or_404(self, key):
        if self.get(key) is None:
            abort(404)
        return self.get(key)

    def filter_by(self, **kwargs):
        for k, v in kwargs.items():
            ans = filter(lambda x: x.k == v, self.values())
            if ans:
                return ans
        return None

    def add(self, arg):
        cursor = self.get_cursor() + 1
        self.setdefault(cursor, arg)

    def deletes(self, key):
        """Perfoms soft delete on specified key - sets key value to None
        :param key: 
        :return: 
        """
        if self.get(key) is None or self.get_cursor() is 0:
            raise Exception("Invalid operation to delete invalid key")

        self.setdefault(key, None)

    def __getitem__(self, item):
        for k, v in self.items():
            if k == item:
                return self[k]
        return None

    def __len__(self):
        return self.get_cursor()


class User():
    def __init__(self, username, email):
        self.username, self.email = username, email

    @property
    def password(self):
        raise AttributeError('Password is not a readable property')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Recipe():
    def __init__(self, title, procedure, user_id):
        self.owner_id = user_id
        self.title = title
        self.description = procedure
        self.createdat = datetime.utcnow

u1 = User(username="Pius", email="npiusdan@gmail.com")
u1.password = "cat"

Users = Query()
Users.add(u1)

Recipes = Query()
