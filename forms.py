from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, RadioField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    name = StringField("Input Pet Name", validators=[InputRequired()])
    species = SelectField("Select Species", validators=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Input Image URL here", validators=[Optional(), URL()])
    age = IntegerField("Age of Animal", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Places any necessary notes here", validators=[Optional(),Length(min=10)])

class EditPetForm(FlaskForm):
    photo_url =  StringField("Update with new photo", validators=[Optional(), URL()])

    notes = TextAreaField('Update pet information', validators= [Optional(), Length(min=10)])

    available= BooleanField("Available?")