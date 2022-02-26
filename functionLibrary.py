"""
This is the Library of All Functions that i will Need
"""

import os , shutil

def containsSubFolders(pathToDirectory):
    """
    This is a Function to Check if a folder "represented by a Path"
    has sub-folders Or NOT , ONLY this
    :return bool
    """
    listOfFolders = os.listdir(pathToDirectory)
    if len(listOfFolders) > 0 :
        return True
    else:
        return False

def allSubPaths(pathToDirectory):
    """
    :param pathToDirectory:
    :return A list of All Folders :
    """
    listOfFolders = os.listdir(pathToDirectory)
    listOfAbsoluteSubPaths = []
    for eachFolder in listOfFolders :
        eachAbsolutePath = os.path.join(pathToDirectory , eachFolder)
        listOfAbsoluteSubPaths.append(eachAbsolutePath)
    return listOfAbsoluteSubPaths





def extractOrDelete(listOfLevelPaths , mainPath) :
    """
    It will Take all Sub Pathes /Absolute
    And then Check , if empty Delete it , else Extract & Delete it Also
    It Returns Nothing ;
    :param listOfLevelPaths:
    """
    for eachPath in listOfLevelPaths :
        try :
            shutil.copytree(eachPath, mainPath, dirs_exist_ok=True)
            shutil.rmtree(eachPath)
        except NotADirectoryError :
            print("ERR")
            # Detected the Error Here ,  it turns to infinite loop 
            pass 
