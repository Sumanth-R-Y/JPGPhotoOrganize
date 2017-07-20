# -*- coding: utf-8 -*-
"""
Rudimentary script to
move .JPG or .jpg files from source folder
to chornological target folders
Date is from the EXIF data
------
Successfully used for Nikon D7100 taken JPG file photos
"""

# IMPORT SECTION
import os
import sys
import time
from PIL import Image
import shutil


#sys.stdout = sys.__stdout__


Source = "E:\\PHOTOS_SOURCE"
Target = "E:\\PHOTOS_TARGET"
LogDir = "E:\\"

Month_Dict = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun',
              '07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}

timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)
logfilename = "log_"+timestr+".txt"
print("Log File Name : "+logfilename)
logfile = LogDir+logfilename
print("Log File Absolute : "+logfile)
logfileptr = open(logfile,"w")

def logprint(str):
    global logfileptr
    logfileptr.write(str+"\n")

logprint ("Image Handler Started ---- "+timestr)
logprint ("Logging for this run  ---- "+logfile)

InitialDir = os.getcwd()

logprint ("Current Directory     ---- "+InitialDir)
logprint("Changing Directory to Source ---- "+Source)

os.chdir(Source)

logprint ("Current Directory     ---- "+os.getcwd())
logprint("Getting the list of files to process ----")

files = os.listdir(Source)

logprint("#Files to process --- "+str(len(files)))
logprint("Finding and processing JPG files .......")
#logprint("Finding and processing JPG files via list comprehension.......")
#list1 =  [[i,Image.open(Source+"\\"+i)._getexif()[36867]] for i in files]
MetaData_List1=[]
count1 = 0
count2 = 0
count3 = 0
exceptioncount=0
for i in files:
    if(i.find(".JPG")>0 or i.find(".jpg")>0):
        count1=count1+1
        x=i
        z=Source+"\\"+i
        try:
            y=Image.open(Source+"\\"+i)._getexif()[36867]
        except TypeError as err:
            exceptionerror="TypeError: {0}".format(err)
            logprint("Error on "+i+" ---" +exceptionerror)
            exceptioncount=exceptioncount+1
            continue
        except KeyError as err:
            exceptionerror="KeyError: {0}".format(err)
            logprint("Error on "+i+" ---" +exceptionerror)
            exceptioncount=exceptioncount+1
            continue
        else:
            MetaData_List1.append([x,y,y[0:4],y[5:7],z,Target+"\\"+y[0:4]+"\\"+y[5:7]+Month_Dict[y[5:7]]])
            count2=count2+1
    else:
        logprint("Filename rejected --- " + i)
        count3=count3+1
logprint("Total Files rejected by name: "+str(count3))
logprint("Total Files accepted by name: "+str(count1))
logprint("Total Successfully Processed:"+str(count2)+" ----- Type or Key Errors encountered"+str(exceptioncount))
logprint("Compare sums ---- Total Files:"+str(len(files))+" ---- "+str(count3+count1))
        
'''        
MetaData_List = [[x,y,y[0:4],y[5:7],z,Target+"\\"+y[0:4]+"\\"+y[5:7]+Month_Dict[y[5:7]]] 
         for x,y,z in 
         [[i,Image.open(Source+"\\"+i)._getexif()[36867],Source+"\\"+i] 
          for i in files if(i.find(".JPG") >0 )]]
'''

logprint("Generating data from MetaData of JPG -----")
[logprint(each[0]+" --- "+each[1]+" --- "+each[2]+" --- "+each[3]+" --- "+each[4]+" --- "+each[5]) for each in MetaData_List1]
listyeardir = list(set([each[2] for each in MetaData_List1]))
listmonthdir = list(set([each[3]+Month_Dict[each[3]] for each in MetaData_List1]))
listfilenameunique = list(set([each[5] for each in MetaData_List1]))
#[logprint(each) for each in listfilenameunique]
for each in  listfilenameunique:
    #print(os.path.isdir(each),os.path.exists(each))
    if (os.path.isdir(each)):
        logprint(each + " --- Already Exists")
    else:
        logprint(each + " --- Do Not Exist ... Creating it")
        os.makedirs(each)
        

for each in MetaData_List1:
    #logprint("Copying "+each[4]+" to "+each[5]+" as " + each[0])
    #shutil.copy(each[4],each[5])
    shutil.move(each[4],each[5])


'''
for i in files:
    if(i.find(".JPG") >0 ):
        t1 = Source+"\\"+i
        t2 = Image.open(t1)._getexif()[36867]
        year1 = t2[0:4]
        month1 = t2[5:7]
        logprint(i+" ---- "+t2+" ---- " + Target+"\\"+year1+"\\"+Month_Dict[month1])
  '''     

        
        
'''
Target = "E:\\PHOTOS_TARGET"
try:
    os.mkdir("E:\\PHOTOS_1")
except OSError as err:
    a="OS error: {0}".format(err)
    print(a)
    if (a.find("[WinError 183] Cannot create a file when that file already exists:") > 0):
        pass
    else:
        '''
    
logfileptr.flush()
logfileptr.close() 
