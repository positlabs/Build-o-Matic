#!/usr/bin/env python

import os
import shutil
import time
import re

#TODO - get rid of globals - use returns instead
#TODO - minify inline script

global indexhtml

config = {}
indexhtml = ""
newHTML = ""
compiledScripts = []
sourcePaths = []
scriptIndexes = []  # keep track of where we pulled the scripts from
scriptRegex = r'<!--.*build-o-matic .*(?=\.js)'

tmpdir = "temp_js"
compiled = "%s/*.js" % tmpdir


# scrape script tag groups for file names and compile them
def getScriptGroups():
    global scriptIndexes
    global indexhtml
    global newHTML
    timestamp = "?" + str(int(round(time.time() / 1000)))

    while re.search(scriptRegex, indexhtml):
        getScriptGroup()

    newHTML = indexhtml
    offset = 0
    for s in compiledScripts:
        tag = "\t<script type='text/javascript' src='" + s.split(config["root"])[1] + timestamp + "'></script>\n"
        newHTML = newHTML[:scriptIndexes[0]+offset] + tag + newHTML[scriptIndexes[0]+offset:]
        scriptIndexes = scriptIndexes[1:]
        offset += len(tag)
        # output new html with tag groups replaced by compiled scripts

    # newHTML = indexhtml[:scriptIndex] + newScripts + indexhtml[scriptIndex:]


    # newHTML = indexhtml[:scriptIndex] + newScripts + indexhtml[scriptIndex:]


def getScriptGroup():
    global indexhtml
    global scriptIndexes
    global sourcePaths

    start = re.search(scriptRegex, indexhtml).start(0)
    end = indexhtml[start:].find('/build-o-matic') + 18
    scriptBlock = indexhtml[start:end + start]
    scriptIndexes.append(start)

    # get the name of the script group
    scriptName = indexhtml[start:].split("build-o-matic ")[1].split(".js")[0] + ".js"

    print "-------------------"
    print "compiling block: " + scriptName
    print "-------------------"

    # print scriptBlock.split("<script")
    for item in scriptBlock.split("<script")[1:]:
        # get src attributes
        src = item.split("src=")[1][1:].split(".js")[0]
        sourcePaths.append(config["root"] + src + ".js")
        # print "src",src

    # remove this block from indexhtml
    indexhtml = indexhtml.replace(scriptBlock, "")

    output = config["root"] + config["js"] + scriptName
    compiledScripts.append(output)
    buildFiles(sourcePaths, output)
    sourcePaths = []


def clean():
    try:
        shutil.rmtree(tmpdir)
        os.rmdir(tmpdir)
    except Exception, e:
        pass


def prepare():
    try:
        os.mkdir(tmpdir)
    except:
        os.rmdir(tmpdir)
        os.mkdir(tmpdir)


def compileFiles(files):
    for _file in files:
        fOut = os.path.join(tmpdir, os.path.split(_file)[1])
        print "    %s -> %s" % (_file, fOut)
        os.system("uglifyjs -nc -o %s %s" % (fOut, _file))


def assemble(output):
    a = open(output, 'w')
    a.write("// COMPILED SCRIPTS\n\n")
    for fi in sourcePaths:
        filepath = os.path.join(tmpdir, fi.split("/")[-1])
        f = open(filepath, 'r')
        a.write("// Original file: %s\n" % os.path.split(fi)[1])
        a.write(f.read())
        a.write("\n")
    a.close()


def buildFiles(mfiles, mOutput):
    prepare()
    compileFiles(mfiles)
    assemble(mOutput)
    clean()


def run(html):
    global indexhtml
    indexhtml = html
    getScriptGroups()
    return newHTML


