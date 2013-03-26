#!/usr/bin/env python

import glob, os, sys, shutil

import config

indexhtml = open(config.root + config.index).read()
compiledScripts = []
scriptIndex = 0 # keep track of where we pulled the scripts from

# scrape script tag groups for file names and compile them
def getScriptGroups():
    while(indexhtml.find('<!-- build') != -1):
        getScriptGroup()
        
    global indexhtml
    newScripts = ""
    for s in compiledScripts:
        tag = "<script type='text/javascript' src='" + s.split(config.root)[1] + "'></script>\n"
        newScripts += tag
    # output new html with tag groups replaced by compiled scripts
    indexhtml = indexhtml[:scriptIndex] + newScripts + indexhtml[scriptIndex:]
    os.system("touch " + config.root + "production.html")
    f = open(config.root + "production.html", "w")
    f.write(indexhtml)
    f.close()
    print "created " + config.root + "production.html"
    
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
    






tmpdir = "temp_js"
compiled = "%s/*.js" % tmpdir

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
        os.system("uglifyjs -o %s %s" % (fo, file))

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


def compile():
    getScriptGroups()


