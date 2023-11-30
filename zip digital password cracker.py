import itertools
import os
import zipfile
import time
import datetime
import shutil
import easygui

os.chdir(os.getenv("temp"))

if os.path.exists("zip_crack"):
    shutil.rmtree("zip_crack")
os.mkdir("zip_crack")
os.chdir(os.getenv("temp")+"\zip_crack")

file=easygui.fileopenbox("zip file",default=r"C:\Users\%username%\Downloads")
if file == None:
    exit()

def trypassword(pwd):
    try:
        with zipfile.ZipFile(file) as i:
            i.extractall("./",pwd=pwd.encode("utf-8"))
        return True
    except:
        return False

def mode1():
    global start_time
    start_time = time.time()
    digits = "0123456789"
    password_length = 1 

    while True:
        passwords = itertools.product(digits, repeat=password_length)

        for password in passwords:
            password = "".join(password) 
            print("\rtry:", password,end="")
            if trypassword(password):
                print("")
                return(password)

        password_length += 1


def mode2(len):
    global start_time
    start_time = time.time()
    digits = "0123456789"
    password_length = int(len)

    passwords = itertools.product(digits, repeat=password_length)

    for password in passwords:
        password = "".join(password) 
        print("\rtry:", password,end="")
        if trypassword(password):
            print("")
            return(password)
            
know_len=input("Do you know the password length (Y/N)?")

if know_len.upper() == "Y":
    print("Cracked successfully, password:"+mode2(input("Password length:")))
else:
    print("Cracked successfully, password:"+mode1())

print("Crack time:",datetime.timedelta(seconds=(time.time())-start_time))

try:
    os.chdir(os.getenv("temp"))
    shutil.rmtree("zip_crack")
except:
    pass

input()