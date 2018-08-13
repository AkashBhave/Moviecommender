import urllib.request
import zipfile
import os

def getDataset(datasetType):
    smallDatasetName = "ml-latest-small"
    bigDatasetName = "ml-latest"
    smallDatasetNewName = "data-small"
    bigDatasetNewName = "data-big"
    smallDatasetURL = "http://files.grouplens.org/datasets/movielens/" + smallDatasetName + ".zip"
    bigDatasetURL = "http://files.grouplens.org/datasets/movielens/" + bigDatasetName + ".zip"

    if datasetType == "small":
        if not checkDataset(smallDatasetNewName): downloadDataset(smallDatasetURL, smallDatasetName, smallDatasetNewName)
    else:
        if not checkDataset(bigDatasetNewName): downloadDataset(bigDatasetURL, bigDatasetName, bigDatasetNewName)


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

def main():
    getDataset("small")

if __name__ == '__main__':
    main()