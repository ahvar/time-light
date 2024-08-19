"""
------------------------------
Models
------------------------------
The data that will be stored in the database will be represented by a collection of classes, usually called
database models. 

------------------------------
Object Relational Mapper (ORM)
------------------------------
The ORM, SQLAlchemy, allows applications to manage a database using high-level entities such as classes,
objects and methods instead of tables and SQL. B/c SQLAlchemy supports multiple relational databases,
the application can be developed with a lightweight db (e.g. SQLite) that does not require a server and
go to production with a more robust production db with server (e.g. PostgreSQL, MySQL) without any changes
to the application.
"""

from typing import Optional

# an extension that provides a Flask-friendly wrapper to SQLAlchemy
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class User(db.Model):
    """
    The User class created above will represent users stored in the database. The class inherits from db.Model,
    a base class for all models from Flask-SQLAlchemy. The User model defines several fields as class variables.
    These are the columns that will be created in the corresponding database table.

    Fields are assigned a type using Python type hints, wrapped with SQLAlchemy's so.Mapped generic type.
    A type declaration such as so.Mapped[int] or so.Mapped[str] define the type of the column,
    and also make values required, or non-nullable in database terms. To define a column that is allowed to be
    empty or nullable, the Optional helper from Python is also added, as password_hash demonstrates.
    """

    # column configured as primary key
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        """
        How to print Users
        """
        return "<User {}>".format(self.username)
