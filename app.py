from flask import (render_template, url_for, request, redirect)
from models import db, Project, app
from datetime import datetime


# Create a route for the application
@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects = projects)


# Create a route for id project
@app.route("/project/<id>")
def project(id):
    project = Project.query.get_or_404(id)
    return render_template("detail.html", project = project)


# Create a route for add a new project
@app.route("/project/new", methods=["GET", "POST"])
def new_project():
    if request.form:
        new_project = Project(
            title=request.form["title"],
            description=request.form["desc"],
            date_created = datetime.strptime(request.form["date"], "%Y-%m").date(),
            skills=request.form["skills"],
            github=request.form["github"]
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("projectform.html")


# Create a route for edit a project
@app.route("/project/<id>/edit", methods=["GET", "POST"])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form["title"]
        project.description = request.form["desc"]
        project.date_created = datetime.strptime(request.form["date"], "%Y-%m").date()
        project.skills = request.form["skills"]
        project.github = request.form["github"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", project = project)


# Create a route for delete a project
@app.route("/project/<id>/delete")
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))


# Create a 404 route
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", msg=error), 404


# Create a about route
@app.route("/about")
def about():
    projects = Project.query.all()
    return render_template("about.html", projects = projects)


# Create a dunder main function for th
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")