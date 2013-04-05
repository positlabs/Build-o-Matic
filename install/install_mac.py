#!/usr/bin/env python

# Build-o-Matic dependency installer for mac

import os, shutil, subprocess

def install():
    packages = ["less", "clean-css", "uglify-js@1"]

    print "=================="
    print "installing npm, less, clean-css, and ugligy-js, ImageOptim"
    print "=================="

    try:
        npmVersion = subprocess.check_output("npm --version", shell=True)
    except:
        npmVersion = 0
        
    print "npm version: " + npmVersion
    
    if(npmVersion == 0):
        # TODO - Does npm depend on nodejs?
        # install npm
        os.system("sudo curl https://npmjs.org/install.sh | sudo sh")

    # install libs available through npm
    for p in packages:
        os.system("sudo npm install -g %s" % p)
        
    if(os.path.exists("/Applications/ImageOptim.app") == False):
        # download ImageOptim, extract, and install
        os.system("sudo curl -O http://imageoptim.com/ImageOptim.tbz2")
        os.system("tar -xjvf ImageOptim.tbz2")
        shutil.move("ImageOptim.app", "/Applications/ImageOptim.app")
        os.remove("ImageOptim.tbz2")
        

if(__name__ == "__main__"):
    install()
