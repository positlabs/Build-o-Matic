#!/usr/bin/env python

import glob, os, sys, shutil, time
import config

indexhtml = ""
tmpdir = "temp_css"
linkIndex = 0
# compiled = "%s/*.css" % tmpdir

def clean():
	print "Cleaning the tmp directory"
	try:
		shutil.rmtree(tmpdir)
		os.rmdir(tmpdir)
	except Exception, e:
		pass

def prepare():
	print "Creating the temp directory"
	os.mkdir(tmpdir)

def compile(files, output):
	compiled = []
	
	for file in files:
		filename = file.split("/")[-1]
		print filename
		if(filename.find('.less') != -1):
			os.system("lessc %s %s" % (file, os.path.join(tmpdir, "tmp_" + filename)))
			os.system("cleancss -o %s %s" % (os.path.join(tmpdir, "clean_" + filename), os.path.join(tmpdir, "tmp_" + filename)))
		else:
			os.system("cleancss -o %s %s" % (os.path.join(tmpdir, "clean_" + filename), file))
			
		compiled.append(os.path.join(tmpdir, "clean_" + filename));
	assemble(output, compiled)

def assemble(output, compiled):
	print "Copying CSS to target %s" % config.css
	a = open(output, 'w+')
	a.write("/* COMPILED CSS */\n\n")
	for fi in compiled:
		f = open(fi, 'r')
		a.write("/* Original file: %s */\n" % os.path.split(fi)[1].split("clean_")[1])
		a.write(f.read())
		a.write("\n")
	a.close()
	
def getStyleGroup():
    global indexhtml
    global linkIndex
    print "-------------------"
    # get the name of the script group
    linkName = indexhtml.split("style ")[1].split(" -->")[0]
    print "compiling block: " + linkName
    print "-------------------"
    
    start = indexhtml.find('<!-- style')
    end = indexhtml.find('/style -->') + 11
    linkIndex = start
    linkBlock = indexhtml[start:end]
    # print linkBlock
    
    global scriptIndex
    scriptIndex = start
    
    sourcePaths = []
    for item in linkBlock.split("<link")[1:]:
        # get href attributes
        href = item.split("href=\"")[1].split("\"")[0]
        sourcePaths.append(config.root + href)
    
    # remove this block from indexhtml
    indexhtml = indexhtml.replace(indexhtml[start:end], "")

    output = config.root + config.css + linkName
#    compiledLinks.append(output)
    compile(sourcePaths, output)
    return config.css + linkName
	
def run(html):
	global indexhtml
	indexhtml = html

	compiled = []

# 	get link tag groups
	while(indexhtml.find('<!-- style') != -1):
		compiled.append(getStyleGroup())
		
	clean()

# 	insert new link tags in production.html
	timestamp = "?" + str(int(round(time.time()/1000)))
	for file in compiled:
		tag = "\t<link rel='text/css' href='" + file + timestamp + "'/>\n"
		indexhtml = indexhtml[:linkIndex] + tag + indexhtml[linkIndex:]
	
	return indexhtml
	
	
