"""
This is the Library of All Functions that i will Need
"""

from distutils.errors import DistutilsFileError
from genericpath import isdir
import os
import shutil
import distutils.dir_util


def containsSubFolders(pathToDirectory):
    """
    This is a Function to Check if a folder "represented by a Path"
    has sub-folders Or NOT , ONLY this
    :return bool
    """
    listOfFoldersAndFiles = os.listdir(pathToDirectory)
    #  The List Contains Folders Names && Files TOO

    pathesToFilesFolders = []
    for eachItem in listOfFoldersAndFiles:
        pathesToFilesFolders.append(os.path.join(pathToDirectory, eachItem))
        # Now we Have a list of all paths
        # Whether Files pathes or Folders pathes  ;
    foldersOnlyList = returnFoldersOnly(pathesToFilesFolders)
    if len(foldersOnlyList) > 0:
        return True
    else:
        return False


def returnFoldersOnly(pathesToFilesFolders):
    foldersOnly = []
    for eachPath in pathesToFilesFolders:
        if isdir(eachPath):
            foldersOnly.append(eachPath)
    return foldersOnly


def allSubPaths(pathToDirectory):
    """
    :param pathToDirectory:
    :return A list of All Folders :
    """
    listOfFolders = os.listdir(pathToDirectory)
    listOfAbsoluteSubPaths = []
    for eachFolder in listOfFolders:
        eachAbsolutePath = os.path.join(pathToDirectory, eachFolder)
        listOfAbsoluteSubPaths.append(eachAbsolutePath)
    return listOfAbsoluteSubPaths


def extractOrDelete(listOfLevelPaths, mainPath):
    """
    It will Take all Sub Pathes /Absolute
    And then Check , if empty Delete it , else Extract & Delete it Also
    It Returns Nothing ;
    :param listOfLevelPaths:
    """
    for eachPath in listOfLevelPaths:
        try:
            # shutil.copytree(eachPath, mainPath, dirs_exist_ok=True)
            distutils.dir_util.copy_tree(eachPath, mainPath)
            shutil.rmtree(eachPath)
        except DistutilsFileError:
            print("ERR")
            break
            # Detected the Error Here ,  it turns to infinite loop
