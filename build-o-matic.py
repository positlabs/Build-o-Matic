#!/usr/bin/env python

import config, sys

sys.path.append("modules")
import optimg, compile_js, compile_styles, deploy, html_util

if (config.input == config.output):
    print "-" * 20
    print "Error: config.input and config.output should have different names"
    print "-" * 20
    sys.exit()

args = sys.argv[1:]

devHTML = open(config.root + config.input).read()

# optimizes all images in the image directory
optimg.run(config.root + config.images)
devHTML = html_util.removeComments(devHTML)
devHTML = compile_js.run(devHTML)
devHTML = compile_styles.run(devHTML)
devHTML = html_util.removeWhitespace(devHTML)


def writeFile(html):
    f = open(config.root + config.output, "w+")
    f.write(html)
    f.close()
    print "\ncreated " + config.root + config.output

writeFile(devHTML)

if ("deploy" in args):
    print "-" * 20
    print "deploying to " + config.ftpRoot
    deploy.upload()
    
