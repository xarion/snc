import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Group(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))

    def __init__(self, name):
        super(Group, self).__init__()
        self.name = name

    @staticmethod
    def create(name):
        group = Group(name)
        db.session.add(group)
        db.session.commit()
