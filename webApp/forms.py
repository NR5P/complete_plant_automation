from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, DateField
from wtforms_components import TimeField
from wtforms.validators import DataRequired, Length
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Timer import Timer
from automation_controller.Lights import Lights
import datetime


class ValveForm(FlaskForm):
    valveName = StringField("Name", validators=[DataRequired(), Length(min=1, max=100)])
    valveNotes = TextAreaField("Notes", validators=[Length(max=300)])
    valveOnOff = SelectField("on/off", choices=[("True", "on"), ("False", "off")])
    valveCycleIrrigate = SelectField("cycle or irrigate", choices=[("valveCycle", "cycle"), ("valveIrrigate", "Irrigate")])

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

    selectAll = BooleanField("Select All")
    monday = BooleanField("monday")
    tuesday = BooleanField("tuesday")
    wednesday = BooleanField("wednesday")
    thursday = BooleanField("thursday")
    friday = BooleanField("friday")
    saturday = BooleanField("saturday")
    sunday = BooleanField("sunday")

    daysTuple = (selectAll, monday, tuesday, wednesday, thursday, friday, saturday, sunday)

    submit = SubmitField()


    def setValve(self):
        for valve in IrrigationValve.valveList:
            valve.name = self.valveName
            valve.notes = self.valveNotes
            valve.on = self.valveOnOff
            valve.cycleOrIrrigate = self.valveCycleIrrigate

            valve.irrigationTimes[self.valveIrrigationTime] = datetime.timedelta(hours=ValveForm.valveTimeHour,
                                                                                      minutes=ValveForm.valveTimeMinute,
                                                                                      seconds=ValveForm.valveTimeSecond)
            valve.cycleOnTime = datetime.timedelta(hours=ValveForm.cycleOnTimeHour,
                                                   minutes=ValveForm.cycleOffTimeMinute,
                                                   seconds=ValveForm.cycleOnTimeSeconds)
            valve.cycleOffTime = datetime.timedelta(hours=ValveForm.cycleOffTimeHour,
                                                    minutes=ValveForm.cycleOffTimeMinute,
                                                    seconds=ValveForm.cycleOffTimeSeconds)
            valve.blackoutStart = self.blackoutStart
            valve.blackoutStop = self.blackoutStop
            if self.selectAll:
                valve.days.add(ValveForm.daysTuple)
            else:
                for day in ValveForm.daysTuple:
                    if day:
                        valve.days.add(day)





