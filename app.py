from flask import render_template

from models import app, db


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/projects/new")
def add_project():
    return render_template("project-form.html")


@app.route("/projects/<id>")
def project(id):
    return render_template("detail.html")


@app.route("/projects/<id>/edit")
def edit_project(id):
    return render_template("project-form.html")


@app.route("/projects/<id>/delete")
def delete_project(id):
    pass


@app.route("/about")
def about():
    return render_template("about")


@app.errorhandler(404)
def not_found(error):
    return "This is a 404"


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
