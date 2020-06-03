#python prpject
#mehraan kiya
#roshanamooz

import wget
from huepy import *
import urllib

#for example for download www.python.org/download/python 3.8.3/

print("this Is A Simple File Downloader Using Python3\n")

print("Please Insert The link to Your File")


down = input("[+] Inset Link ==> : ")


print("Your Download Will Start soon ; \n")


wget.download(down)


print("Your Downloadig Is Complate")