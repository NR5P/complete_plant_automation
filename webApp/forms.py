from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField, DateField
# from wtforms_components import TimeField
from wtforms.validators import DataRequired, Length
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.IrrigationValve import IrrigationValve
from automation_controller.Timer import Timer
from automation_controller.Lights import Lights
import datetime
from wtforms.fields.html5 import TimeField




class ValveForm(FlaskForm):
    valveName = StringField("Name", validators=[DataRequired(), Length(min=1, max=100)])
    valveNotes = TextAreaField("Notes", validators=[Length(max=300)])
    valveOnOff = SelectField("on/off", choices=[("True", "on"), ("False", "off")])
    valveCycleIrrigate = SelectField("cycle or irrigate", choices=[("cycle", "Cycle"), ("irrigate", "Irrigate")])

    valveIrrigationTime = TimeField("valveIrrigationTime")
    valveTimeHour = StringField("valveTimeHour")
    valveTimeMinute = StringField("valveTimeMinute")
    #valveTimeSecond = StringField("valveTimeSecond")

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

    #submit = SubmitField()


    def setValve(self, valve):
        #for valve in IrrigationValve.valveList:
        valve.name = self.valveName.data
        valve.notes = self.valveNotes
        valve.on = self.valveOnOff
        valve.cycleOrIrrigate = self.valveCycleIrrigate

        valve.irrigationTimes[self.valveIrrigationTime] = datetime.time(hour=self.valveTimeHour,
                                                                        minute=self.valveTimeMinute)
        valve.cycleOnTime = datetime.timedelta(hours=self.cycleOnTimeHour,
                                               minutes=self.cycleOffTimeMinute,
                                               seconds=self.cycleOnTimeSeconds)
        valve.cycleOffTime = datetime.timedelta(hours=self.cycleOffTimeHour,
                                                minutes=self.cycleOffTimeMinute,
                                                seconds=self.cycleOffTimeSeconds)
        valve.blackoutStart = self.blackoutStart
        valve.blackoutStop = self.blackoutStop
        if self.selectAll:
            self.days.add(ValveForm.daysTuple)
        else:
            for day in ValveForm.daysTuple:
                if day:
                    self.days.add(day)

    #TODO can't do these next two functions until i figure out how to tell which valve is submited
    def irrigation_time_add(self):
        valve.irrigationTimes[self.valveIrrigationTime] = datetime.time(hour=self.valveTimeHour,
                                                                        minute=self.valveTimeMinute)

    def irrigation_time_delete(self):
        del valve.irrigationTimes[self.valveIrrigationTime]





