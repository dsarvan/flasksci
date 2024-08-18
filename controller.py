#!/usr/bin/env python

from flask import Flask, render_template, request
from compute import compute
from model import InputForm

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
	else:
		result = None

	return render_template("view.html", form=form, result=result)

if __name__ == "__main__":
	app.run(debug=True)
