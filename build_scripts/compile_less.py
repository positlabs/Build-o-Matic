#!/usr/bin/env python

import glob, os, sys, shutil

lessSrc = "../src/css/src/master.less"
output = "../src/css/compiled/main.css"

tmpdir = "temp_css"
compiled = "%s/*.css" % tmpdir

def clean():
	print "Cleaning the tmp directory"
	try:
		shutil.rmtree(tmpdir)
		os.rmdir(tmpdir)
	except Exception,e:
		pass

def prepare():
	print "Creating the temp directory"
	os.mkdir(tmpdir)

def compile():
	print "Compiling CSS "

	os.system("lessc %s %s" % (lessSrc, os.path.join(tmpdir, "tmp.css") ))
	os.system("cleancss -o %s %s" % ( os.path.join(tmpdir, "clean.css"), os.path.join(tmpdir, "tmp.css") ))

def assemble():
	print "Copying CSS to target %s" % output
	a = open(output, 'w')
	a.write("/* COMPILED CSS */\n\n")
	f = open( os.path.join(tmpdir, "clean.css"), 'r')
	a.write("/* Original file: %s */\n" % os.path.split(lessSrc)[1])
	a.write(f.read())
	a.write("\n")
	a.close()
	
	
def build():
	prepare()
	compile()
	assemble()
	clean()

if(__name__ == '__main__'):
	build()
	print "Done!"