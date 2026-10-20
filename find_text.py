import pathlib
import os
from concurrent.futures import ThreadPoolExecutor


def exits_folder(folder):
  if(os.path.exists(folder)):
   return folder
  else:
   return False


def scan(pah):
   files=[]
   path=exits_folder(pah)
   if(path):
    for file in os.listdir(path):
     if( os.path.isfile(os.path.join(path,file))):
      files.append(os.path.join(path,file))
    return files

def search(text,folder):
   files=scan(folder)
   result=[]
   for file in files:
    with open(file,"r",encoding="utf-8") as f:
     for i, line in enumerate(f,start=1):
      if(text in line):
       result.append([i,file,line.strip()])
   return result

def main(text,folder):
 try:
  with ThreadPoolExecutor(max_workers=10000) as ex:
   future=ex.submit(search,text,folder)
   result=future.result()
  for i in result:
   print(i)
 except:
  print("file not exists")

main("ok","/data/data/com.termux/files/home/tes")
