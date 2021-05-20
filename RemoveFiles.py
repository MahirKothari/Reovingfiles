import time
import os
import shutil
def main():
    deletedFoldersCount = 0
    deletedFilesCOunt = 0
    path = '/users/admin/desktop/folder'
    days = 30
    seconds = time.time()-(days*24*60*60)
    if(os.path.exits(path)):
        for rootfolder,folder,files in os.walk(path):
            if(seconds>=getFileOrFolderAge(rootfolder)):
                removeFolder(rootfolder)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folderpath = os.path.join(rootfolder,folder)
                    if(seconds>=getFileOrFolderAge(folderpath)):
                        removeFolder(folderpath)
                        deletedFoldersCount+=1
                 for file in files:
                    filepath = os.path.join(rootfolder,file)
                    if(seconds>=getFileOrFolderAge(filepath)):
                        removeFile(filepath)
                        deletedFilesCount+=1
        else:
            if(seconds>=getFileOrFolderAge(filepath)):
                        removeFile(filepath)
                        deletedFilesCount+=1
    else:
        deletedFilesCount+=1
    print(deletedFilesCount,deletedFoldersCount)
def removeFiles(path):
    if not os.remove(path):
        print('removed Successfully')
    else:
        print('unable to delete')
def removeFolders(path):
    if not shutil.rmtree(path):
        print('removed Successfully')
    else:
        print('unable to delete')
def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime
    return(ctime)
main()

