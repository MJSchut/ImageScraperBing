"""ImageScraper: Search for an image and download to folder."""
__author__ = "MJ Schut"

from dirmaker import DirMaker
from imagescraper import ImageScraper

# variables
verbose = True
searchTerm = "GOB"
imageAmount = 100

# Step 1. Make reference image folder
if verbose:
    print "Generating image folders..."

dirMaker = DirMaker(verbose=verbose)
photoDir = dirMaker.make_dir(childDir=searchTerm)

if verbose:
    print "Photo directory: %s" % photoDir
    print "...Image folders generated"

# Step 2. Download images
if verbose:
    print "Downloading %i images of %s..." % (
        imageAmount,
        searchTerm)

imageScraper = ImageScraper(
    searchTerm,
    photoDir,
    imageAmount=imageAmount,
    verbose=verbose)
imageScraper.scrape()

if verbose:
    print "...Finished downloading images"
