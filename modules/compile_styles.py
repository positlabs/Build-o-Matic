#!/usr/bin/env python

import os
import shutil
import time
import re

#TODO - get rid of globals, use returns
config = {}
indexhtml = ""
tmpdir = "temp_css"
linkIndex = 0
styleRegex = r'<!--.*build-o-matic .*(?=\.css)'

# compiled = "%s/*.css" % tmpdir



def clean():
    try:
        shutil.rmtree(tmpdir)
        os.rmdir(tmpdir)
    except Exception, e:
        pass


def prepare():
    print "Creating the temp directory"
    os.mkdir(tmpdir)


def compileStyles(files, output):
    compiled = []

    for _file in files:
        filename = _file.split("/")[-1]
        print filename
        if (filename.find('.less') != -1):
            os.system("lessc %s %s" % (_file, os.path.join(tmpdir, "tmp_" + filename)))
            os.system("cleancss -o %s %s" % (
                os.path.join(tmpdir, "clean_" + filename), os.path.join(tmpdir, "tmp_" + filename)))
        else:
            os.system("cleancss -o %s %s" % (os.path.join(tmpdir, "clean_" + filename), _file))

        compiled.append(os.path.join(tmpdir, "clean_" + filename))
    assemble(output, compiled)


def assemble(output, compiled):
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
    # get the name of the script group


    start = re.search(styleRegex, indexhtml).start(0)
    end = indexhtml[start:].find('/build-o-matic') + 18
    linkBlock = indexhtml[start:end+start]
    linkIndex = start
    # print linkBlock

    linkName = indexhtml[start:].split("build-o-matic ")[1].split(".css")[0] + ".css"

    print "-------------------"
    print "compiling block: " + linkName
    print "-------------------"
    # print linkBlock


    sourcePaths = []
    for item in linkBlock.split("<link")[1:]:
        # get href attributes
        href = re.search(r'.*\.less|.*\.css', item.split("href=")[1][1:]).group(0)
        sourcePaths.append(os.path.join(config["root"], href))
        # print 'href', href

    # remove this block from indexhtml
    indexhtml = indexhtml.replace(linkBlock, "")

    output = os.path.join(os.path.join(config["root"], config["css"]),  linkName)
    compileStyles(sourcePaths, output)
    return config["css"] + linkName


def run(html):
    global indexhtml
    indexhtml = html

    compiled = []

    # 	get link tag groups
    while re.search(styleRegex, indexhtml):
        compiled.append(getStyleGroup())

    clean()

    # 	insert new link tags in production.html
    timestamp = "?" + str(int(round(time.time() / 1000)))
    for _file in compiled:
        tag = "\t<link rel='text/css' href='" + _file + timestamp + "'/>\n"
        indexhtml = indexhtml[:linkIndex] + tag + indexhtml[linkIndex:]

    return indexhtml
	
	
