import os
import shutil
from time import sleep


def main ():
    print("Welcome to AutoPanel")
    sleep (2)
    print("""
        1- Folder Operations
        2- File Operations
        3- Execute Specific Commands Manually 
    """)
    choix = int(input("======> : "))
    if (choix == 1):
        print("""1- Create Folder \n2- Delete Folder
        """)
        folderOption = int(input(": ")) 
        path = input("Enter Path to Your Folder : ")
        if (folderOption == 1):
            if  os.path.exists(path):
                fname = input("Enter Folder Name : ")
                fpath = os.path.join(path,fname)
                os.mkdir(fpath)
                sleep(1)
                print(fname,"Created Succefully Go to :",fpath)

            else : 
                print("ERROR Path Invalid Please Check it")
                
        if (folderOption == 2):
            if os.path.exists(path):
                fname = input("Enter Folder Name : ")
                fpath = os.path.join(path,fname)
                shutil.rmtree(fpath)

    if (choix == 2):
        print("""1- Create File \n2- Delete File
        """)
        FileOption = int(input(": "))
        path = input("Enter Path to Your File : ")
        if (FileOption == 1):
            fname = input("Enter File Name : ")
            extension = input("File extension : ")
            fname = fname+'.'+extension
            fpath = os.path.join(path,fname)
            if not os.path.exists(fpath):
                f= open(fpath,'a')
                sleep(1)
                print(fname,"Created Succefully Go to :",fpath)
        
        if(FileOption == 2):
            fname = input("Enter File Name : ")
            fpath = os.path.join(path,fname)
            if not os.path.exists(fpath):
                os.remove(fpath)
                sleep (1)
                print(fname,"Deleted Succefully Go To :",path)


    if(choix == 3):
        Cname = input("Enter Your Command : ")
        os.system(Cname)


main()

