#!/usr/bin/env python

import config, os, optimg, compile_js

#optimizes all images in the image directory
optimg.run(config.root + config.images)
compile_js.compile()









