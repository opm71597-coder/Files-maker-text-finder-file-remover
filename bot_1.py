import random
import os
import subprocess
char="abcdefghiFhgwodjwihejwkjavbHcwjiyTerqpxbcNvxnn"
comman_lenth=6

def use_():
  if(os.path.exists("use.txt")):
   with open("use.txt","r") as file :
    database=file.read()
   return database
  else:
   return ""

def save_database(data):
  with open("use.txt","a") as f:
   f.write(data+"\n")


def make_filename():
  use=use_()
  name=""
  for i in range(comman_lenth):
   name+=random.choice(char)
  if(name not in use):
   save_database(name)
   return name+".txt"

def save_file(name):
  with open(name,"w") as f:
   f.write("")

def add_contant(name,contant):
 if(os.path.exists(name)):
  with open(name,"a") as f:
   f.write(contant+"\n")



def make_files(comtant,num):
   use=use_()
   if(comtant.lower().strip()=="random"):
    for i in range(1000):
     name=make_filename()
     save_file(name)
     for x in range(199):
      con=random.choice(char)
      add_contant(name,con)
    


make_files("random","susj")

