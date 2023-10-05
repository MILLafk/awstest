from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['UPLOADED_IMAGES_DEST'] = 'uploads'

db = SQLAlchemy(app)
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    path = db.Column(db.String(255))

@app.route('/')
def index():
    images = Image.query.all()
    return render_template('index_img.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        if image:
            image_path = images.save(image)
            image_name = image.filename
            new_image = Image(name=image_name, path=image_path)
            db.session.add(new_image)
            db.session.commit()
    return redirect(url_for('index'))

@app.route('/image/<int:id>')
def view_image(id):
    image = Image.query.get(id)
    if image:
        return send_from_directory('uploads', image.path)
    return 'Image not found'

@app.route('/delete/<int:id>', methods=['POST'])
def delete_image(id):
    image = Image.query.get(id)
    if image:
        # Delete the image file from the file system
        os.remove(os.path.join(app.config['UPLOADED_IMAGES_DEST'], image.path))
        
        # Remove the image from the database
        db.session.delete(image)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
