import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("title", db.String())
    date = db.Column("created_at", db.DateTime)
    description = db.Column("description", db.Text)
    skills = db.Column("skills", db.Text)
    github_repo = db.Column("github_link", db.Text)

    def __repr__(self):
        return f"""<Project (title: {self.title})>"""
