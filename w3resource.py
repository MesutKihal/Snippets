import os
import sys
import struct
import platform
import site
import multiprocessing
import pickle
import getpass
import time
import glob

#Get system mode

if sys.maxsize > 2**32: print("64bits")
else: print("32bits")

    #Or

print(struct.calcsize("P")*8) #it prints 32 or 64

#Get os name, platform, and release info

print(os.name())
print(platform.system())
print(platform.release())

#site-packages folder

print(site.getsitepackages())

#running an external command

print(os.system("ls"))

#get cpu number

print(multiprocessing.cpu_count())

#save and load data

pickle.dump(['rar,zip,zipx,tar','txt,pdf,doc,docx,html,htm,odt,xls,xlsx,ods,ppt,pptx','mp3,wav,flac,aiff,alac,aac,wma,ogg','apk,app,bin,cmd,mst,exe','mp4,mov,wmv,flv,avi,mkv','bmp,jpg,tiff,tif,gif,png'], open('formats.dat', 'wb'))
print(pickle.load(open('formats.dat', 'rb')))

#access environment variables

print(os.environ)
print(os.environ['HOME'])
print(os.environ['PATH'])

#get username

print(getpass.getuser())

#get the absolute file path

print(os.path.abspath("w3resource.py"))

#get file creation and date of modification

print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

#get all txt files

files = glob.glob("*.txt")

