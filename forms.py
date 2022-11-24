from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField('Pet Name: ', validators=[InputRequired(message='PLEASE ENTER A PET NAME')])
    species = StringField('Pet Species: ', validators=[InputRequired(message='PLEASE ENTER A SPECIES NAME'), AnyOf(['dog','cat','porcupine'],message="Only dogs, cats, or porcupine allowed")])
    photo = StringField('Pet Photo URL: ', validators=[Optional(), URL()])
    age = FloatField('Pet Age: ', validators=[Optional(), NumberRange(min=0, max=30,message="Age must be within 0 and 30")])
    notes = StringField('Notes: ', validators=[Optional()])

class EditPetForm(FlaskForm):
    photo = StringField('Pet Photo URL: ', validators=[Optional(), URL()])
    notes = StringField('Notes: ', validators=[Optional()])
    available = BooleanField('Available: ',default = 'checked')