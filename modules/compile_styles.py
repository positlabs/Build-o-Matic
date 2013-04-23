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


# https://github.com/cloudhead/less.js/wiki/Command-Line-Usage
def compileStyles(files, output):
    compiled = []

    for _file in files:
        filename = _file.split("/")[-1]
        print _file

        if (filename.find('.less') != -1):

            originalDirs = _file.split("/")[:-1]
            outputDirs = output.split("/")[:-1]

            # need to compare depth of output with depth of input
            # if they are the same, pass nothing as rootpath
            if len(originalDirs) == len(outputDirs):
                prependPath = ""
            elif len(originalDirs) > len(outputDirs):
                # prepend path needs to point to original dir from output dir
                # original deeper, add path to original
                sliceFrom = len(originalDirs) - len(outputDirs)
                prependPath = "/".join(originalDirs[-sliceFrom:])
            else:
                # original shallower, add ../ for each level
                prependPath = "../" * (len(outputDirs) - len(originalDirs))
                pass

            # print "lessc -x -rp=%s -ru %s %s" % (rootpath, _file, os.path.join(tmpdir, "clean_" + filename))
            if(len(prependPath) > 0):
                os.system("lessc -x -rp=%s %s %s" % (prependPath, _file, os.path.join(tmpdir, "clean_" + filename)))
            else:
                os.system("lessc %s %s -x" % (_file, os.path.join(tmpdir, "clean_" + filename)))
        else:
            #TODO - just use less compiler so we can trash the cleancss dependency
            os.system("cleancss -o %s %s" % (os.path.join(tmpdir, "clean_" + filename), _file))

        compiled.append(os.path.join(tmpdir, "clean_" + filename))
    assemble(output, compiled)

def assemble(output, compiled):
    subdirs = output.split("/")[:-1]

    if len(subdirs) > 0:
        try:
            os.makedirs("/".join(subdirs))
        except:
            pass

    a = open(output, 'w+')
    a.write("/* COMPILED CSS */\n\n")
    for fi in compiled:
    	print fi
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
    linkBlock = indexhtml[start:end + start]
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

    output = os.path.join(os.path.join(config["root"], config["css"]), linkName)
    compileStyles(sourcePaths, output)
    return os.path.join(config["css"], linkName)


def run(html):
    global indexhtml
    indexhtml = html

    compiled = []

    prepare()

    # 	get link tag groups
    while re.search(styleRegex, indexhtml):
        compiled.append(getStyleGroup())

    clean()

    # 	insert new link tags in production.html
    timestamp = "?" + str(int(round(time.time() / 1000)))
    for _file in compiled:
        tag = "\t<link rel='stylesheet' type='text/css' href='" + _file + timestamp + "'/>\n"
        indexhtml = indexhtml[:linkIndex] + tag + indexhtml[linkIndex:]

    return indexhtml
	
	
