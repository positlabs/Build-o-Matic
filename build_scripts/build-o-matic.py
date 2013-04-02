#!/usr/bin/env python

import config, os, sys, optimg, compile_js, compile_styles, deploy

if(config.input == config.output):
    print "-"*20
    print "Error: config.input and config.output should have different names"
    print "-"*20
    sys.exit()
    
args = sys.argv[1:]


devHTML = open(config.root + config.input).read()

# optimizes all images in the image directory
optimg.run(config.root + config.images)
devHTML = compile_js.run(devHTML)
devHTML = compile_styles.run(devHTML)

def writeFile(html):
    f = open(config.root + config.output, "w+")
    f.write(html)
    f.close()
    print "created " + config.root + config.output

writeFile(devHTML)

if("deploy" in args):
    print "-"*20
    print "deploying to " + config.ftpRoot
    deploy.upload()
    
