import datetime
from flask import render_template, redirect, url_for, request

from models import app, db, Project


@app.route("/")
def index():
    projects = Project.query.all()

    return render_template("index.html", projects=projects)


@app.route("/projects/new", methods=["GET", "POST"])
def add_project():
    if request.form:
        try:
            project_date = request.form["date"]
            project_datetime = datetime.datetime.strptime(project_date, "%Y-%m-%d")

            new_project = Project(
                title=request.form["title"],
                date=project_datetime,
                description=request.form["desc"],
                skills=request.form["skills"],
                github_repo=request.form["github"]
            )

            db.session.add(new_project)
            db.session.commit()

            return redirect(url_for("index"))

        except Exception:
            print("Something went wrong")

    return render_template("add-project.html")


@app.route("/projects/<id>")
def project(id):
    project = Project.query.get_or_404(id)

    formated_date = project.date.strftime("%b %Y")
    project_skills = project.skills.split(",")
    
    return render_template("project.html", project=project, project_date=formated_date, skills=project_skills)


@app.route("/projects/<id>/edit", methods=["GET", "POST"])
def edit_project(id):
    project = Project.query.get_or_404(id)
    formatted_date = project.date.strftime("%Y-%m-%d")

    if request.form:
        try:
            project_date = request.form["date"]
            project_datetime = datetime.datetime.strptime(project_date, "%Y-%m-%d")

            project.title=request.form["title"]
            project.date=project_datetime
            project.description=request.form["desc"]
            project.skills=request.form["skills"]
            project.github_repo=request.form["github"]

            db.session.commit()

            return redirect(url_for("index"))

        except Exception:
            print("Something went wrong")

    return render_template("edit-project.html", project=project, formatted_date=formatted_date)


@app.route("/projects/<id>/delete")
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()

    return redirect(url_for("index"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
