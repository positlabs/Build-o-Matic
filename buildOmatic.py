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

def execute(configpath, doDeploy):
    json_data = open(configpath)

    config = json.load(json_data)
    json_data.close()
    compile_js.config = compile_styles.config = deploy.config = config

    if (config["input"] == config["output"]):
        print "-" * 20
        print "Error: config.input and config.output should have different names"
        print "-" * 20
        sys.exit()

    devHTML = open(config["root"] + config["input"]).read()

    # optimizes all images in the image directory
    # optimg.run(os.path.join(config["root"], config["images"]))
    # devHTML = html_util.removeComments(devHTML)
    # devHTML = compile_js.run(devHTML)
    devHTML = compile_styles.run(devHTML)
    # devHTML = html_util.removeWhitespace(devHTML)


    def writeFile(html):
        f = open(os.path.join(config["root"], config["output"]), "w+")
        f.write(html)
        f.close()
        print "\ncreated ", os.path.join(config["root"], config["output"])

    writeFile(devHTML)

    if (doDeploy):
        print "-" * 20
        print "deploying to " + os.path.join(config["host"], config["ftpRoot"])
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

    if ("deploy" in args):
        doDeploy = True
    else:
        doDeploy = False

    execute(configpath, doDeploy)