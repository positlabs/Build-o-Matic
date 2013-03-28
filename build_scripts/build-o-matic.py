#!/usr/bin/env python

import config, os, optimg, compile_js, compile_styles

devHTML = open(config.root + config.index).read()

#optimizes all images in the image directory
optimg.run(config.root + config.images)
devHTML = compile_js.run(devHTML)
devHTML = compile_styles.run(devHTML)

def writeFile(html):
#    os.system("touch " + config.root + config.output)
    f = open(config.root + config.output, "w+")
    f.write(html)
    f.close()
    print "created " + config.root + config.output

writeFile(devHTML)


