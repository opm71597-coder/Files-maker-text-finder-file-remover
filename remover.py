import os
from concurrent.futures import ThreadPoolExecutor

home=os.listdir()

def remove(exe):
 for file in home:
  if( exe in file):
   os.remove(file)

def main(ed):
 with ThreadPoolExecutor(max_workers=1000) as ex:
  ex.submit(remove,ed)

remove(".txt")
