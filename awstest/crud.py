from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    with app.app_context():
        books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        with app.app_context():
            book = Book(title=title)
            db.session.add(book)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    with app.app_context():
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
