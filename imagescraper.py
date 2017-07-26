"""Imagescraper does the heavy lifting."""
__author__ = "MJ Schut"

import os
import urllib2
import random
import re


class ImageScraper:
    """Imagescraper functions are stored here, call scrape to start."""

    def __init__(self, searchTerm, downloadDir, imageAmount=10, verbose=False):
        """
        Initialize the class with the search term.

        Arguments:
        searchTerm -- A string of the term to be entered into the search
        engine.
        downloaddir -- A string of the path to download the files to.

        Keyword arguments:
        imageAmount -- Integer of amount of images to download.
        verbose -- Set to True if you want a couple of print statements,
        which update you on the progress of the downloading.
        """
        self.searchTerm = searchTerm
        self.downloadDir = downloadDir
        self.imageAmount = imageAmount
        self.verbose = verbose

    def scrape(self):
        """Start the scraping process."""
        page = 0
        query = self.searchTerm
        query = urllib2.quote(query)
        userAgent = ("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US;"
                     "rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7")
        url = ("https://www.bing.com/images/async?q=" + query +
               "&async=content&first=" + str(page))

        headers = {'User-Agent': userAgent}

        searchRequest = urllib2.Request(url, None, headers)
        searchResults = urllib2.urlopen(searchRequest)
        searchData = searchResults.read()

        imageList = re.findall('murl&quot;:&quot;(.*?)&quot;', searchData)
        print imageList
        counter = 0
        if self.verbose:
            print ("Found " + str(len(imageList)) + " images")

        while counter < self.imageAmount:
            index = random.randint(0, len(imageList) - 1)
            imageRequest = urllib2.Request(imageList[index], None, headers)

            try:
                imageRemote = urllib2.urlopen(imageRequest)
                fileName = imageList[index].split('/')[-1]
                if imageRemote.headers.maintype == 'image':
                    f = open(os.path.join(self.downloadDir, fileName), "wb")
                    f.write(imageRemote.read())
                    f.close()

                    if self.verbose:
                        print("Downloaded %i images" % counter + 1)
            except:
                pass
