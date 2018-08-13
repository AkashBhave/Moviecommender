import urllib.request
import zipfile
import os

import pandas as pd
import numpy as np

datasetName = ""


def getDataset(datasetType):
    smallDatasetName = "ml-latest-small"
    bigDatasetName = "ml-latest"
    smallDatasetNewName = "data-small"
    bigDatasetNewName = "data-big"
    smallDatasetURL = "http://files.grouplens.org/datasets/movielens/" + \
        smallDatasetName + ".zip"
    bigDatasetURL = "http://files.grouplens.org/datasets/movielens/" + \
        bigDatasetName + ".zip"

    global datasetName

    if datasetType == "small":
        datasetName = smallDatasetNewName
        if not checkDataset(smallDatasetNewName):
            downloadDataset(smallDatasetURL, smallDatasetName, smallDatasetNewName)
    else:
        datasetName = bigDatasetNewName
        if not checkDataset(bigDatasetNewName):
            downloadDataset(bigDatasetURL, bigDatasetName, bigDatasetNewName)
            


def checkDataset(datasetNewName):
    if(os.path.isdir(datasetNewName)):
        return True
    else:
        return False


def downloadDataset(datasetURL, datasetName, datasetNewName):
    urllib.request.urlretrieve(datasetURL, datasetNewName + ".zip")
    zipExtract = zipfile.ZipFile(datasetNewName + ".zip", 'r')
    zipExtract.extractall()
    zipExtract.close()
    os.rename(datasetName, datasetNewName)
    os.remove(datasetNewName + ".zip")


def readCSV():
    ratingsFrameCols = ["user_id", "movie_id", "rating"]
    ratingsFrame = pd.read_csv(datasetName + "/ratings.csv", sep=",", header=0, names=ratingsFrameCols, usecols=range(3))
    ratingsFrame = ratingsFrame.groupby("movie_id").agg({"rating": [np.size, np.mean]})


def main():
    getDataset("small")
    readCSV()

if __name__ == '__main__':
    main()
