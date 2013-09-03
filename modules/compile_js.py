#!/usr/bin/env python

import os
import subprocess
import re
import time


global indexhtml

closureCompilerPath = "modules/compiler.jar"

config = {}
indexhtml = ""
newHTML = ""
compiledScripts = []
sourcePaths = []
scriptRegex = r'<!--.*build-o-matic .*(?=\.js)'

devRegex = r'<!--\s?dev'
devRegexClose = r'<!--\s?\/dev\s?-->'

#concatenates and minifies js
def minJS(jsFiles, output):
	print "\n" + "=" * 20
	print "minifying ", jsFiles
	print "=" * 20 + "\n"

	args = [
		"java",
		"-jar",
		closureCompilerPath,
		"--js"
	]

	for f in jsFiles:
		args.append(f)

	args.append("--js_output_file")
	args.append(output)

	subprocess.call(args)
	
	print "\n" + "=" * 20
	print "minified output: " + output 
	print "=" * 20 + "\n"

# just concatenates with no minification
def concatJS(jsFiles, output):

	print "\n" + "=" * 20
	print "concatenating : ",  jsFiles 
	print "=" * 20 + "\n"

	a = open(output, 'w')
	
	for fi in jsFiles: 	
		a.write("// Original file: %s\n" % os.path.split(fi)[1])
		out = open(os.path.abspath(fi)).read()
		a.write(out)
		a.write("\n")
		
	a.close()

	print "\n" + "=" * 20
	print "concatenated output: " + output 
	print "=" * 20 + "\n"

def getScriptGroups():
    global indexhtml
    global newHTML

    while re.search(scriptRegex, indexhtml):
        getScriptGroup()

    newHTML = indexhtml

def getScriptGroup():
    global indexhtml
    global sourcePaths

    start = re.search(scriptRegex, indexhtml).start()
    end = indexhtml[start:].find('/build-o-matic') + 18

    scriptBlock = indexhtml[start:end + start]

    # get the name of the script group
    scriptName = indexhtml[start:].split("build-o-matic ")[1].split(".js")[0] + ".js"

    # print scriptBlock.split("<script")
    for item in scriptBlock.split("<script")[1:]:
        # get src attributes
        src = item.split("src=")[1][1:].split(".js")[0]
        sourcePaths.append(config["root"] + src + ".js")

    # remove this block from indexhtml, replace with new tag
    timestamp = "?" + str(int(round(time.time() / 1000)))
    tag = "<script type='text/javascript' src='" + os.path.join(config["js"], scriptName) + timestamp + "'></script>\n"
    indexhtml = indexhtml.replace(scriptBlock, tag)

    output = os.path.join(config["root"], config["js"])
    output = os.path.join(output, scriptName)

    minJS(sourcePaths, output)
    sourcePaths = []

def run(html):
    global indexhtml
    indexhtml = html
    getScriptGroups()
    return newHTML

############################## old

# import os
# import shutil
# import time
# import re

# #TODO - get rid of globals - use returns instead

# global indexhtml

# config = {}
# indexhtml = ""
# newHTML = ""
# compiledScripts = []
# sourcePaths = []
# scriptRegex = r'<!--.*build-o-matic .*(?=\.js)'

# devRegex = r'<!--\s?dev'
# devRegexClose = r'<!--\s?\/dev\s?-->'

# tmpdir = "temp_js"
# compiled = "%s/*.js" % tmpdir


# # scrape script tag groups for file names and compile them
# def getScriptGroups():
#     global indexhtml
#     global newHTML

#     while re.search(scriptRegex, indexhtml):
#         getScriptGroup()

#     newHTML = indexhtml


# def getScriptGroup():
#     global indexhtml
#     global sourcePaths

#     start = re.search(scriptRegex, indexhtml).start()
#     end = indexhtml[start:].find('/build-o-matic') + 18

#     scriptBlock = indexhtml[start:end + start]

#     # get the name of the script group
#     scriptName = indexhtml[start:].split("build-o-matic ")[1].split(".js")[0] + ".js"

#     print "-------------------"
#     print "compiling block: " + scriptName
#     print "-------------------"

#     # print scriptBlock.split("<script")
#     for item in scriptBlock.split("<script")[1:]:
#         # get src attributes
#         src = item.split("src=")[1][1:].split(".js")[0]
#         sourcePaths.append(config["root"] + src + ".js")

#     # remove this block from indexhtml, replace with new tag
#     timestamp = "?" + str(int(round(time.time() / 1000)))
#     tag = "<script type='text/javascript' src='" + os.path.join(config["js"], scriptName) + timestamp + "'></script>\n"
#     indexhtml = indexhtml.replace(scriptBlock, tag)

#     output = os.path.join(config["root"], config["js"])
#     output = os.path.join(output, scriptName)

#     buildFiles(sourcePaths, output)
#     sourcePaths = []


# def clean():
#     try:
#         shutil.rmtree(tmpdir)
#         os.rmdir(tmpdir)
#     except Exception, e:
#         pass


# def prepare():
#     try:
#         os.mkdir(tmpdir)
#     except:
#         shutil.rmtree(tmpdir)
#         os.mkdir(tmpdir)


# def compileFiles(files):
#     for _file in files:
#         fOut = os.path.join(tmpdir, os.path.split(_file)[1])
#         print "    %s -> %s" % (_file, fOut)
#         os.system("uglifyjs -nc -o %s %s" % (fOut, _file))


# def assemble(output):
#     a = open(output, 'w')
#     a.write("// COMPILED SCRIPTS\n\n")
#     for fi in sourcePaths:
#         filepath = os.path.join(tmpdir, fi.split("/")[-1])
#         f = open(filepath, 'r')
#         a.write("// Original file: %s\n" % os.path.split(fi)[1])
#         a.write(f.read())
#         a.write("\n")
#     a.close()


# def buildFiles(mfiles, mOutput):
#     prepare()
#     compileFiles(mfiles)
#     assemble(mOutput)
#     clean()


# def run(html):
#     global indexhtml
#     indexhtml = html
#     getScriptGroups()
#     return newHTML

