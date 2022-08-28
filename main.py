from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "names.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Person(db.Model):
    person_id = db.Column(db.Integer, unique=True, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Name: '{self.first_name}' '{self.last_name}' ID: '{self.person_id}'"


db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.form:
        try:
            person = Person(person_id=request.form.get("person_id"), first_name=request.form.get("first_name"),
                            last_name=request.form.get("last_name"))
            db.session.add(person)
            db.session.commit()
        except Exception as e:
            print("Failed to add person")
            print(e)
    people = Person.query.all()
    return render_template("index.html", people=people)


def is_palindrome(name):
    return name.lower() == name[::-1].lower()


@app.route("/palindrome")
@app.route("/palindrome/<int:person_id>")
def palindrome(person_id):
    person = Person.query.filter_by(person_id=person_id).first()
    return render_template("palindrome_name.html", person=person, palin_first=is_palindrome(person.first_name),
                           palin_last=is_palindrome(person.last_name))


@app.route("/update", methods=["POST"])
def update():
    try:
        person_id = request.form.get("person_id")
        person = Person.query.filter_by(person_id=person_id).first()
        person.first_name = request.form.get("new_first_name")
        person.last_name = request.form.get("new_last_name")
        db.session.commit()
    except Exception as e:
        print("Failed to update person")
        print(e)
    return redirect("/")


@app.route("/delete", methods=["POST"])
def delete():
    person_id = request.form.get("person_id")
    person = Person.query.filter_by(person_id=person_id).first()
    db.session.delete(person)
    db.session.commit()
    return redirect("/")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
