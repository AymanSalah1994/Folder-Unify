import os , shutil

theAbsolutePath = input("Enter the Path of the Directory : ")


# Todo : Checking if the Path is Right/Absolute Or Not  ?

def containsFolder(pathToDirectory):
    """
    This is a Function to Check if a folder "represented by a Path"
    has sub-folders Or NOT , ONLY this
    :return bool
    """

    listOfFolders = os.listdir(pathToDirectory)
    if listOfFolders:
        return True
    else:
        return False





def allSubPaths(pathToDirectory):
    """
    :param pathToDirectory:
    :return A list of All Folders :
    """
    listOfFolders = os.listdir(pathToDirectory)
    listOfAbsolutePaths = []
    for eachFolder in listOfFolders :
        eachAbsolutePath = os.path.join(pathToDirectory , eachFolder)
        listOfAbsolutePaths.append(eachAbsolutePath)
    return listOfAbsolutePaths


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
            pass

        # Check if folder empty and Delete it ?
        # CHeck if full , Empty & delete

def engine():
    while True:
        subFolders = allSubPaths(theAbsolutePath)
        extractOrDelete(subFolders , theAbsolutePath)
        if containsFolder(theAbsolutePath) :
            continue
        else:
            break

engine()