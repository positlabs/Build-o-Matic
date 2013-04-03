#!/usr/bin/env python

import config, os, datetime
from calendar import timegm

from ftplib import FTP

def upload():
    
    ftp = FTP(config.host, config.username, config.password)
    
    try:
        ftp.mkd(config.ftpRoot[:-1])
    except:
        pass
    
    # change working dir on ftp to project root    
    ftp.cwd(config.ftpRoot)
    
    for root, dirs, files in os.walk(config.root):
        
        # make directory structure
        for dir in dirs: 
            try:
                dirPath = os.path.join(root, dir)
                dirPath = dirPath.split(config.root)[1]
                ftp.mkd(dirPath)
            except:
                pass
        
        # upload the files
        for file in files:
            # ignoring hidden files and directories like .git and .DS_Store
            if(file.find(".") != 0):

                td = 1
                localMTime = int(os.stat(os.path.join(root, file)).st_mtime)

                try:
                    remoteFile = os.path.join(root.split(config.root)[1], file)
                    remoteMTime = str(ftp.sendcmd("MDTM %s" % remoteFile)[3:].strip())
                    remoteMTime = mdtmToDate(remoteMTime)
#                    print "local:\t", localMTime
#                    print "remote:\t", remoteMTime
                    td = localMTime - remoteMTime
                except Exception,e:
#                    print Exception, e
                    pass
                
                if(td > 0):
                    localFile = os.path.join(root, file)
                    remoteFile = os.path.join(root.split(config.root)[1], file)
                    print localFile, "\t-->\t", config.ftpRoot + remoteFile
                    ftp.storbinary("STOR " + remoteFile, open(localFile))
    
    ftp.quit()
    ftp.close()   


def mdtmToDate(mdmt):
    yy = int(mdmt[:4])
    mm = int(mdmt[4:6])
    dd = int(mdmt[6:8])
    hh = int(mdmt[8:10])
    mn = int(mdmt[10:12])
    ss = int(mdmt[12:14])
    dttm = datetime.datetime(yy,mm,dd,hh,mn,ss)
    return timegm(dttm.utctimetuple())
