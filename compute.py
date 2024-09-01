#!/usr/bin/env python

from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import matplotlib
matplotlib.use('SVG')

plt.style.use("classic")
plt.rc("text", usetex="True")
plt.rc("figure", titlesize=12)
plt.rc("pgf", texsystem="pdflatex")
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("font", family="serif", weight="normal", size=12)


def damped_vibrations(t, A, b, w):
	return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
	"""return filename of plot of the damped_vibrations function"""
	t = linspace(0, T, resolution+1)
	u = damped_vibrations(t, A, b, w)
	fig, ax = plt.subplots() # needed to avoid adding curves in plot
	ax.plot(t, u, "r", lw=1)
	ax.grid(True, which="both")
	ax.set(xlabel="$t$", ylabel="$u(t)$")
	ax.set_title(f"$A = {A}\,m, b = {b}\,kg{{\cdot}}s^{{-1}}, w = {w:.2f}\,s^{{-1}}$")
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		# remove old plot files
		for filename in glob.glob(os.path.join('static', '*.svg')):
			os.remove(filename)

	# use time in filename that the browser has not chached
	plotfile = os.path.join('static', str(time.time()) + '.svg')
	plt.savefig(plotfile)
	return plotfile

if __name__ == '__main__':
	print(compute(1, 0.1, 1, 20))
