#
# Makefile.inc -- Makefile Targets und Variablen für Papers
#
# Achtung: dieses File wird erzeugt vom Skript scripts/mkmakefile
#
# (c) 2020 Prof Dr Andreas Müller, Hochschule Rapperswil
#
PAPERFILES = \
	papers/part2.tex \
	papers/uebersicht.tex \
	papers/000template/main.tex \
	papers/vanderpol/main.tex \
	papers/logistic/main.tex \
	papers/kettenbruch/main.tex \
	papers/taylor/main.tex \
	papers/fem/main.tex \
	papers/burgers/main.tex \
	papers/pade/main.tex \
	papers/qr/main.tex \
	papers/laplace/main.tex \
	papers/perturbation/main.tex \
	papers/quadratur/main.tex \
	papers/steps/main.tex \
	papers/francis/main.tex \
	papers/legendre/main.tex \
	papers/cg/main.tex \
	papers/ew/main.tex \
	papers/ableitung/main.tex \
	papers/arctan/main.tex \
	papers/interdiff/main.tex \
	
buch1-blx.bbl:	buch1-blx.aux
	bibtex buch1-blx

buch2-blx.bbl:	buch2-blx.aux
	bibtex buch2-blx

buch3-blx.bbl:	buch3-blx.aux
	bibtex buch3-blx

buch4-blx.bbl:	buch4-blx.aux
	bibtex buch4-blx

buch5-blx.bbl:	buch5-blx.aux
	bibtex buch5-blx

buch6-blx.bbl:	buch6-blx.aux
	bibtex buch6-blx

buch7-blx.bbl:	buch7-blx.aux
	bibtex buch7-blx

buch8-blx.bbl:	buch8-blx.aux
	bibtex buch8-blx

buch9-blx.bbl:	buch9-blx.aux
	bibtex buch9-blx

buch10-blx.bbl:	buch10-blx.aux
	bibtex buch10-blx

buch11-blx.bbl:	buch11-blx.aux
	bibtex buch11-blx

buch12-blx.bbl:	buch12-blx.aux
	bibtex buch12-blx

buch13-blx.bbl:	buch13-blx.aux
	bibtex buch13-blx

buch14-blx.bbl:	buch14-blx.aux
	bibtex buch14-blx

buch15-blx.bbl:	buch15-blx.aux
	bibtex buch15-blx

buch16-blx.bbl:	buch16-blx.aux
	bibtex buch16-blx

buch17-blx.bbl:	buch17-blx.aux
	bibtex buch17-blx

buch18-blx.bbl:	buch18-blx.aux
	bibtex buch18-blx

buch19-blx.bbl:	buch19-blx.aux
	bibtex buch19-blx

buch20-blx.bbl:	buch20-blx.aux
	bibtex buch20-blx

buch21-blx.bbl:	buch21-blx.aux
	bibtex buch21-blx

BLXFILES = buch.bbl \
	buch1-blx.bbl \
	buch2-blx.bbl \
	buch3-blx.bbl \
	buch4-blx.bbl \
	buch5-blx.bbl \
	buch6-blx.bbl \
	buch7-blx.bbl \
	buch8-blx.bbl \
	buch9-blx.bbl \
	buch10-blx.bbl \
	buch11-blx.bbl \
	buch12-blx.bbl \
	buch13-blx.bbl \
	buch14-blx.bbl \
	buch15-blx.bbl \
	buch16-blx.bbl \
	buch17-blx.bbl \
	buch18-blx.bbl \
	buch19-blx.bbl \
	buch20-blx.bbl \

PAPER_DIRECTORIES = \
	000template \
	vanderpol \
	logistic \
	kettenbruch \
	taylor \
	fem \
	burgers \
	pade \
	qr \
	laplace \
	perturbation \
	quadratur \
	steps \
	francis \
	legendre \
	cg \
	ew \
	ableitung \
	arctan \
	interdiff \
	
PAPER_MAKEFILEINC = \
	papers/000template/Makefile.inc \
	papers/vanderpol/Makefile.inc \
	papers/logistic/Makefile.inc \
	papers/kettenbruch/Makefile.inc \
	papers/taylor/Makefile.inc \
	papers/fem/Makefile.inc \
	papers/burgers/Makefile.inc \
	papers/pade/Makefile.inc \
	papers/qr/Makefile.inc \
	papers/laplace/Makefile.inc \
	papers/perturbation/Makefile.inc \
	papers/quadratur/Makefile.inc \
	papers/steps/Makefile.inc \
	papers/francis/Makefile.inc \
	papers/legendre/Makefile.inc \
	papers/cg/Makefile.inc \
	papers/ew/Makefile.inc \
	papers/ableitung/Makefile.inc \
	papers/arctan/Makefile.inc \
	papers/interdiff/Makefile.inc \
	
