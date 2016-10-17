

import os

def rename_file():
    file_list = os.listdir(r"E:\swa")
    saved_path = os.getcwd()
    print "Current working directory is "+ saved_path
    os.chdir(r"E:\swa")

    for file_name in file_list:
        print "Old file name "+ file_name + "New file name "+ file_name.translate(None,"0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_file()
