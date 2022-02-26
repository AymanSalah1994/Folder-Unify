import os
import shutil
from functionLibrary import containsSubFolders, allSubPaths, extractOrDelete
theAbsolutePath = input("Enter the Path of the Directory : ")

# Todo : Checking if the Path is Right/Absolute Or Not  ?


def engine():
    working = containsSubFolders(theAbsolutePath)
    if working : 
        subFolders = allSubPaths(theAbsolutePath)
        extractOrDelete(subFolders, theAbsolutePath)
        engine()
        

engine()
