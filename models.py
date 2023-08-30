from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

stock_photo = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

class Pet(db.Model):
    """Model for the pets"""

    __tablename__="pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = True, default = stock_photo)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Text, nullable = False, default=True)

    def image_url(self):
        return self.photo_url or stock_photo
