#!/usr/bin/env python

import os

def run(imgDir):
    if(os.path.exists("/Applications/ImageOptim.app")):
        os.system("open -a /Applications/ImageOptim.app " + imgDir)
    else:
        os.system("trimage --quiet -d " + imgDir)
        
            
