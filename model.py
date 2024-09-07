#!/usr/bin/env python

import functools
from wtforms import Form, FloatField, validators
from math import pi

def check_interval(form, field, min_value=None, max_value=None):
	"""Form validation: failure if value is outside an interval"""
	if min_value is not None:
		failure = True if field.data < min_value else False
	if max_value is not None:
		failure = True if field.data > max_value else False

	if failure:
		raise validators.ValidationError(
			f"{field.name} = {field.data} not in [{'-infty' if min_value is None else min_value}, {'infty' if max_value is None else max_value}]")

def interval(min_value=None, max_value=None):
	return functools.partial(check_interval, min_value=min_value, max_value=max_value)

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
		validators=[validators.InputRequired(), interval(0, None)])

	b = FloatField(
		label='damping factor (kg/s)', default=0,
		validators=[validators.InputRequired(), interval(0, None)])

	w = FloatField(
		label='frequency (1/s)', default=2*pi,
		validators=[validators.InputRequired()])

	T = FloatField(
		label='time interval (s)', default=20,
		validators=[validators.InputRequired(), check_T])
