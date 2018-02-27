from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.secret_key = os.urandom(32)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(15), unique=True)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def get_contacts():
    return render_template('index.html', contacts=Contacts.query.all())

@app.route('/new', methods=['GET', 'POST'])
def create_contact():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['phone']:
            flash('Please enter all the fields', 'error')
        else:
            contact = Contacts(request.form['name'],
                               request.form['email'],
                               request.form['phone'])
            db.session.add(contact)
            db.session.commit()

            flash('Contact was successfully submitted')

            return redirect(url_for('get_contacts'))

    return render_template('new.html')


if __name__ == '__main__':
        app.run(
        host="0.0.0.0",
        port=8080
  )

