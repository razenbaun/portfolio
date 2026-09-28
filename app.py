from flask import Flask, render_template, abort
from data.certificates import CERTIFICATES
from data.projects import PROJECTS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/certificates")
def certificates():
    return render_template("certificates.html", certificates=CERTIFICATES)


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = next((p for p in PROJECTS if p["slug"] == slug), None)
    if project is None:
        abort(404)
    return render_template("project_detail.html", project=project)


if __name__ == "__main__":
    app.run(debug=True)