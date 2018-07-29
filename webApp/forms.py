from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, TimeField, BooleanField
from wtforms.validators import DataRequired, Length


class ValveForm(FlaskForm):
    valveName = StringField("valveName", validators=[DataRequired(), Length(min=1, max=100)])
    valveNotes = TextAreaField("valveNotes", validators=[Length(max=300)])
    valveOnOff = SelectField("valveOnOff", choices=[("valveOn", "on"), ("valveOff", "off")])
    valveCycleIrrigate = SelectField("valveCycleIrrigate", choices=[("valveCycle", "cycle"), ("valveIrrigate", "Irrigate")])

    valveIrrigationTime = TimeField("valveIrrigationTime")
    valveTimeHour = StringField("valveTimeHour")
    valveTimeMinute = StringField("valveTimeMinute")
    valveTimeSecond = StringField("valveTimeSecond")

    cycleOnTimeHour = StringField("cycleOnTimeHour")
    cycleOnTimeMinute = StringField("cycleOnTimeMinute")
    cycleOnTimeSeconds = StringField("cycleOnTimeSecond")

    cycleOffTimeHour = StringField("cycleOffTimeHour")
    cycleOffTimeMinute = StringField("cycleOffTimeMinute")
    cycleOffTimeSeconds = StringField("cycleOffTimeSecond")

    blackoutStart = TimeField("blackoutStart")
    blackoutStop = TimeField("blackoutStop")

    monday = BooleanField("monday")
    tuesday = BooleanField("monday")
    wednesday = BooleanField("monday")
    thursday = BooleanField("monday")
    friday = BooleanField("monday")
    saturday = BooleanField("monday")
    sunday = BooleanField("monday")


