#!/usr/bin/env python

from wtforms import Form, FloatField, validators
from math import pi

def check_T(form, field):
	"""Form validation: failure if T > 30 periods"""
	w = form.w.data
	T = field.data
	period = 2*pi/w

	if T > 30*period:
		nperiod = int(round(T/period))
		raise validators.ValidationError(
			f"Cannot plot as much as {nperiod} period! T < {30*period:.0f}")

class InputForm(Form):
	A = FloatField(
		label='amplitude (m)', default=1.0,
		validators=[validators.InputRequired(), validators.NumberRange(0, 1E+20)])

	b = FloatField(
		label='damping factor (kg/s)', default=0,
		validators=[validators.InputRequired()])

	w = FloatField(
		label='frequency (1/s)', default=2*pi,
		validators=[validators.InputRequired()])

	T = FloatField(
		label='time interval (s)', default=6*pi,
		validators=[validators.InputRequired(), check_T])
