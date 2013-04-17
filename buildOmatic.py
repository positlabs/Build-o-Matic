#!/usr/bin/env python

"""

    usage: ./buildOmatic.py path/to/config.json deploy
    "deploy" argument is optional - it uploads the site to an ftp

"""

import json
import sys

sys.path.append("modules")
import optimg
import compile_js
import compile_styles
import deploy
import html_util
import os

def execute(config, doDeploy, doOptimg):

    if (config["input"] == config["output"]):
        print "-" * 20
        print "Error: config.input and config.output should have different names"
        print "-" * 20
        sys.exit()

    devHTML = open(config["root"] + config["input"]).read()

    if(doOptimg == True):
        optimg.run(os.path.join(config["root"], config["images"]))
    devHTML = html_util.removeComments(devHTML)
    devHTML = compile_js.run(devHTML)
    devHTML = compile_styles.run(devHTML)
    devHTML = html_util.removeWhitespace(devHTML)


    def writeFile(html):
        f = open(os.path.join(config["root"], config["output"]), "w+")
        f.write(html)
        f.close()
        print "\ncreated ", os.path.join(config["root"], config["output"])

    writeFile(devHTML)

    if (doDeploy):
        upload()

def upload():
    print "-" * 20
    print "deploying to " + os.path.join(deploy.config["host"], deploy.config["ftpRoot"])
    deploy.upload()

if __name__ == "__main__":
    # TODO - maybe make args more flexible. maybe use argparse

    configpath = ""
    args = sys.argv[1:]
    try:
        configpath = args[0]
    except:
        print "\nFIRST ARGUMENT MUST BE PATH TO CONFIG.JSON!\n"
        quit()

    json_data = open(configpath)
    config = json.load(json_data)
    json_data.close()
    compile_js.config = compile_styles.config = deploy.config = config

    if '-D' in args:
        #hard deploy, don't build project
        upload()

    elif '-O' in args:
        #hard img optim, don't build project
        optimg.run(os.path.join(config["root"], config["images"]))

    else:
        if "--deploy" in args or "-d" in args:
            doDeploy = True
        else:
            doDeploy = False

        if "--optimg" in args or "-o" in args:
            doOpt = True
        else:
            doOpt = False


        execute(config, doDeploy, doOpt)