from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()

@app.route('/')
def show_pets():
    """ Displays All Pets """
    pets = Pet.query.all()
    return render_template('show_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_new_pet():
    """ Adds a new pet if form is submitted and redirects to the homepage """
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, age=age, photo_url=photo, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_new_pet.html', form = form)

@app.route('/<int:pid>', methods=['GET', 'POST'])
def show_and_edit_pet(pid):
    """ Shows selected pet details and allows modifcation of the photo, notes, and availability """
    pet = Pet.query.get_or_404(pid)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('show_pet_and_edit.html', form=form, pet=pet)

