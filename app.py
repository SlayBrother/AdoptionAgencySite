from flask import Flask, render_template, redirect, flash, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app=Flask(__name__)


app.config['SECRET_KEY'] = "colby123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptionagency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    """Lists all pets like it is the home page"""
    pets = Pet.query.all()
    return render_template('list_pet.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_new_pet():
    """This route will add a new pet to our table"""
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(name=form.name.data, age=form.age.data, species=form.species.data, photo_url=form.photo_url.data, notes=form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} added.')
        return redirect(url_for('list_pets'))
    else:
        return render_template("add.html", form=form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_post():
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f'{pet.name} has been edited')
        return redirect(url_for('list_pets'))
    else:
        return render_template('/pet_edit_form.html', form=form, pet=pet)
    
@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    pet=Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)