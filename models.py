from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a model class for adding and editing project information
# Connect to the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///projects.db"
db = SQLAlchemy(app)


# The database should already contain at least the 4 previous projects of the Techdegree
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    description = db.Column("Description", db.Text())
    date_created = db.Column("Date Created", db.Date)
    skills = db.Column("Skills", db.String())
    github = db.Column("GitHub Link", db.String())
    
    def __rep___(self):
        return f"""<Project (Name: {self.title}
        Description: {self.description}
        Date Created: {self.date_created}
        Skills: {self.skills}
        GitHub Link: {self.github})"""