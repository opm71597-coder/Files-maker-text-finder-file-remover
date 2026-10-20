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


def make_contant_random(len):
 con=""
 for i in range(1,len):
  con+=random.choice(char)
 return con

def make_files_random():
    use=use_()
    for i in range(random.randint(1,100)):
     name=make_filename()
     if(name not in use):
      save_file(name)
      for x in range(random.randint(1,100)):
       con=make_contant_random(random.randint(1,100))
       add_contant(name,con)


def make_files(how,lines,contant):
 use=use_()
 for i in range(how):
  name=make_filename()
  if(name not in use):
   save_file(name)
   for i in range(lines):
    add_contant(name,contant)


#make_files_random()
def main():
  mode=input("enter mode :")
  if(mode.lower().strip()=="random"):
   make_files_random()
  else:
   try:
    fils=int(input("enter how  files you make : "))
    lines=int(input("enter how lines in files you need : "))
    con=input("what contant you need to add :")
    make_files(fils,lines,con)
   except ValueError:
    print("invalid input")

main()
