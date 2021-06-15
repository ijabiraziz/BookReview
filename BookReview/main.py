from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Subscirbe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200),  nullable=False, unique=True)
    message = db.Column(db.String(200))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def home_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    client = Subscirbe(name=name, email=email, message=message)

    db.session.add(client)
    db.session.commit()

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=False)
