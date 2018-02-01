
from asyncio import sleep

import pyarrow.parquet as pq
import os, fnmatch
# parquet_file = pq.ParquetFile('./parq/0_0_0.parquet')
import time
import re


def getAllFilesInSub(start):
    fileList = []
    for path, subdirs, files in os.walk(start):
        for name in files:
            if name.startswith('week'):
                #print(path)
                removeNf(path,name,4)
                fileList.append(os.path.join(path, name))
    return fileList

def removeNf(path,fileName,n=4):
    newName=fileName[n:]
    print(os.path.join(path,newName))
    os.rename(os.path.join(path,fileName),os.path.join(path,newName))

def main():
    iFilePath = '/home/andres/hadoopindus/testid/tests/sql/'
    getAllFilesInSub(iFilePath)

if __name__ == '__main__':
    main()



