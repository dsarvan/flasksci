#!/usr/bin/env python

import sys
from flask import Flask, render_template, request
from model import InputForm

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    form = InputForm(request.form)
    if request.method == "POST" and form.validate():
        result = compute(form.A.data, form.b.data, form.w.data, form.T.data)
    else:
        result = None

    return render_template(template, form=form, result=result)


if __name__ == "__main__":
    svg = True if sys.argv == "svg" else False

    if svg:
        from compute import compute_svg as compute
        template = "view_svg.html"

    else:
        from compute import compute_png as compute
        template = "view_png.html"

    app.run(debug=True)
