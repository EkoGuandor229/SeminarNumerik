#
# Makefile -- build the book cover
#
# (c) 2018 Prof Dr Andreas Müller, Hochschule Rapperswil
#
all:	buchcover.png

buchcover.pdf:	buchcover.tex
	pdflatex buchcover.tex

buchcover.png:	buchcover.pdf Makefile
	convert -density 300 -extract 1966x2900+2630+190 buchcover.pdf \
		buchcover.png

nozzle.jpg:	nozzle.png
	convert nozzle.png -density 300 -units PixelsPerInch -flop nozzle.jpg
