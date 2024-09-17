#!/usr/bin/env python

import argparse
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

    return render_template(TEMPLATE, form=form, result=result)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Damped sinusoidal wave")
    parser.add_argument("--fmt", choices=["png", "svg"], default="png", help="Image file format")

    args = parser.parse_args()

    if args.fmt == "png":
        from compute import compute_png as compute
        TEMPLATE = "view_png.html"

    if args.fmt == "svg":
        from compute import compute_svg as compute
        TEMPLATE = "view_svg.html"

    app.run(debug=True)
