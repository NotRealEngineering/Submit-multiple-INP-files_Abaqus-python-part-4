#Property of Not Real Engineering 
#Copyright 2020 Not Real Engineering - All Rights Reserved You may not use, 
#           distribute and modify this code without the written permission 
#           from Not Real Engineering.
############################################################################
##             Submitting INP files                                       ##
############################################################################

from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *


No_of_Jobs = 11    # Set number of Jobs here


for q in range (1,No_of_Jobs):
    INPfilename='Job-%d' %(q)       # set odb name here
    path='./'                       # set odb path here (if in working dir no need to change!)
    INPpath=path+INPfilename+'.inp'    

    mdb.ModelFromInputFile(inputFileName=INPpath
        , name='Model-%d' %(q) )
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-%d' %(q), modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Job-%d' %(q), nodalOutputPrecision=SINGLE, 
        numCpus=1, queue=None, scratch='', type=ANALYSIS, userSubroutine='', 
        waitHours=0, waitMinutes=0)
        
    mdb.jobs['Job-%d' %(q) ].submit(consistencyChecking=OFF) 
    mdb.jobs['Job-%d' %(q) ].waitForCompletion()    

#Property of Not Real Engineering 
