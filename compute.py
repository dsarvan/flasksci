#!/usr/bin/env python

import base64
from io import BytesIO
from numpy import exp, cos, linspace
from matplotlib.figure import Figure
import os, time, glob
import matplotlib.style
import matplotlib as mpl

mpl.use("Agg")
mpl.style.use("classic")
mpl.rc("text", usetex="True")
mpl.rc("figure", titlesize=12)
mpl.rc("pgf", texsystem="pdflatex")
mpl.rc("axes", labelsize=14, titlesize=14)
mpl.rc("font", family="serif", weight="normal", size=12)


def damped_vibrations(t, A, b, w):
    return A * exp(-b * t) * cos(w * t)


def compute(A, b, w, T, resolution):
    t = linspace(0, T, resolution + 1)
    u = damped_vibrations(t, A, b, w)
    fig = Figure()  # needed to avoid adding curves in plot
    ax = fig.subplots()
    ax.plot(t, u, "r", lw=1)
    ax.grid(True, which="both")
    ax.set(xlim=(0, T), ylim=(-A, A))
    ax.set(xlabel="$t$", ylabel="$u(t)$")
    ax.set_title(f"$A = {A}\,m, b = {b}\,kg{{\cdot}}s^{{-1}}, w = {w:.2f}\,s^{{-1}}$")
    return fig


def compute_png(A, b, w, T, resolution=1000):
    """return filename of plot of the damped_vibrations function"""

    fig = compute(A, b, w, T, resolution)

    # make Matplotlib write to BytesIO file object
    # and grab return the object's string
    figfile = BytesIO()  # save it to a temporary buffer file
    fig.savefig(figfile, format="png")
    figdata_png = base64.b64encode(figfile.getvalue()).decode()
    return figdata_png


def compute_svg(A, b, w, T, resolution=1000):
    """return filename of plot of the damped_vibrations function"""

    fig = compute(A, b, w, T, resolution)

    # make Matplotlib write to BytesIO file object
    # and grab return the object's string
    figfile = BytesIO()  # save it to a temporary buffer file
    fig.savefig(figfile, format="svg")
    figdata_svg = "<svg" + figfile.getvalue().decode().split("<svg")[1]
    return figdata_svg
