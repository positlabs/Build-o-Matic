#!/usr/bin/env python

import config, os
from ftplib import FTP

def upload():
    
    ftp = FTP(config.host, config.username, config.password)
    
    try:
        ftp.mkd(config.ftpRoot[:-1])
    except:
        "continue"
    
    # change working dir on ftp to project root    
    ftp.cwd(config.ftpRoot)
    
    for root, dirs, files in os.walk(config.root):
        
        # make directory structure
        for dir in dirs: 
            try:
                dirPath = root + "/" + dir
                dirPath = dirPath.split(config.root)[1]
                ftp.mkd(dirPath)
            except:
                "continue"
        
        # upload the files
        for file in files:
            # ignoring hidden files and directories like .git and .DS_Store
            if(file.find(".") != 0):
                
                separator = "/"
                if(len(root.split(config.root)[1]) == 0):
                    separator = ""
                
                localFile = root + "/" + file
                remoteFile = root.split(config.root)[1] + separator + file
                print localFile, "\t-->\t", config.ftpRoot + remoteFile
                ftp.storbinary("STOR " + remoteFile, open(localFile))
    
    ftp.quit()
    ftp.close()   
