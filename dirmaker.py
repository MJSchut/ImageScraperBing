"""dirmaker.py: Make directories."""
__author__ = "MJ Schut"

import os


class DirMaker:
    """All variables are stored in this class for convience."""

    def __init__(self, verbose=False):
        """
        Initialize the class.

        Arguments:
        verbose -- Set to True if you want a couple of print statements,
        which update you on the progress of the downloading.
        """
        self.dirlist = []
        self.verbose = verbose

    def make_dir(self, childDir="default", parentDir=os.getcwd()):
        """
        Make a new directory.

        Keyword arguments:
        childDir -- A string of name of the directory that will be made.
        You can name this whatever you want, as long as it doesn't conflict
        with folder naming conventions of your os. Defaults to "default".
        parentDir -- A string containing the path of the root directory.
        Defaults to the current working directory
        """
        nDir = os.path.join(parentDir, childDir)

        if nDir in self.dirlist:
            print ("The directory %s at path %s was already part of the "
                   "dirlist!\nReturning..." % (childDir, parentDir))
            return nDir
        self.dirlist.append(nDir)
        if os.path.exists(nDir):
            if self.verbose:
                print ("The directory %s at path %s already "
                       "exists!\nReturning..." % (childDir, parentDir))
            return nDir
        os.makedirs(nDir)
        return nDir
