#!/usr/bin/env python

import glob, os, sys, shutil, time

import config

indexhtml = ""
newHTML = ""
compiledScripts = []
scriptIndex = 0  # keep track of where we pulled the scripts from

tmpdir = "temp_js"
compiled = "%s/*.js" % tmpdir


# scrape script tag groups for file names and compile them
def getScriptGroups():
    while(indexhtml.find('<!-- build') != -1):
        getScriptGroup()
        
    global indexhtml
    global newHTML
    newScripts = ""
    timestamp = "?" + str(int(round(time.time()/1000)))

    for s in compiledScripts:
        tag = "\t<script type='text/javascript' src='" + s.split(config.root)[1] + timestamp + "'></script>\n"
        newScripts += tag
    # output new html with tag groups replaced by compiled scripts
    newHTML = indexhtml[:scriptIndex] + newScripts + indexhtml[scriptIndex:]


def getScriptGroup():
    global indexhtml
    print "-------------------"
    # get the name of the script group
    scriptName = indexhtml.split("build ")[1].split(" -->")[0]
    print "compiling block: " + scriptName
    print "-------------------"
    
    start = indexhtml.find('<!-- build')
    end = indexhtml.find('/build -->') + 10
    scriptBlock = indexhtml[start:end]
    # print scriptBlock
    
    global scriptIndex
    scriptIndex = start
    
    sourcePaths = []
    for item in scriptBlock.split("<script")[1:]:
        # get src attributes
        src = item.split("src=\"")[1].split("\"")[0]
        sourcePaths.append(config.root + src)
#        print src
    
    # remove this block from indexhtml
    indexhtml = indexhtml.replace(indexhtml[start:end], "")

    output = config.root + config.js + scriptName
    compiledScripts.append(output)
    buildFiles(sourcePaths, output)
    

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

def compileFiles(files):
    for file in files:
        fo = os.path.join(tmpdir, os.path.split(file)[1])
        print "    %s -> %s" % (file, fo)
        os.system("uglifyjs -nc -o %s %s" % (fo, file))

def assemble(output):
    print "Copying js to target %s" % output
    a = open(output, 'w')
    a.write("// COMPILED SCRIPTS\n\n")
    for fi in glob.glob(compiled):
        f = open(fi, 'r')
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


