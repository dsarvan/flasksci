#!/usr/bin/env python

from wtforms import Form, FloatField, validators

class InputForm(Form):
	r = FloatField(validators=[validators.InputRequired()])
