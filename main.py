#!/usr/bin/env python3
import os
try:
  import argparse
  import time
  import sys
  import getopt
  import subprocess

  import sys
  from sys import platform
  import json
  import base64
  import shutil

  from tqdm import tqdm
  import urllib.request
except:
  print("Installing dependencies of build...")
  os.system("pip install tqdm")
  os.system("pip install getopt")
  os.system("pip install argparse")

vars = {}


def download(url, filename):
    import functools
    import pathlib
    import shutil
    import requests
    import tqdm

    r = requests.get(url, stream=True, allow_redirects=True)
    if r.status_code != 200:
        r.raise_for_status()  # Will only raise for 4xx codes, so...
        raise RuntimeError(f"Request to {url} returned status code {r.status_code}")
    file_size = int(r.headers.get('Content-Length', 0))

    path = pathlib.Path(filename).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)

    desc = "(Unknown total file size)" if file_size == 0 else ""
    r.raw.read = functools.partial(r.raw.read, decode_content=True)  # Decompress if needed
    with tqdm.tqdm.wrapattr(r.raw, "read", total=file_size, desc=desc) as r_raw:
        with path.open("wb") as f:
            shutil.copyfileobj(r_raw, f)

    return path




def pbar(r,sl=0.02):
  for i in tqdm(range(r)):
      time.sleep(sl)

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

def send_help():
    print('USAGE: build [options]')
    print('A build tool created by Ehnryu\n')
    print('Basic options:\n')
    print('--help : this command\n')
    print('--build : build project\n')
    print('--sendargs :send args to buildfile\n')
    print('--runfunc : run a specialised function\n')

def printc(color,*text):
  CEND      = '\33[0m'
  print(color + text[0] + CEND)



def run(command):
    subprocess.check_output(command,shell=True)

def build():
    advanced = ["sendargs =","runfunc =","build"]


    argv = sys.argv[1:]
    opts = []


    try:
      opts, args = getopt.getopt(argv, "hr:",advanced)


    except:
        printc(CRED,"ERROR: Invalid arguments provided.")
        send_help()

    for opt, arg in opts:
        opt = opt.rstrip()
        opt = opt.replace(" ","")

        if opt in ["-h","--help"]:
          send_help()
        if opt in ["--sendargs"]:
          return {"x":"t","args":sys.argv}
        if opt in ["--build"]:
          return {"x":"t","args":args}
        if opt in ["--runfunc","-r"]:
          return {"x":"t","args":args,"func":arg}






x = build()

def default(x):
  if x != None:
    if x["x"] == "t":
      args = x["args"]
      argz = ""
      for item in args:
        if item not in ["build","build.py","main.py","--sendargs"]:
          if item != args[len(args)-1]:
            argz += f"{item},"
          else:
            argz += f"{item}"
      files = []
      for file in os.listdir(os.getcwd()):
        files.append(file)
      if "Buildfile" in files:
        xylo = False
        tex = ""
        line = 0
        function = ""
        printc(CVIOLET,"Running build ...")
        f = open("Buildfile", "r")
        try:
          func = x["func"]
        except KeyError:
          func = False
        cs = True
        s = False
        for item in f.readlines():
          if func != False:
            
            if s == False:
              cs = False
              
              if item.lower().rstrip() == (f"@function {func}:"):
                cs = True
                s = True
          if cs:
            iten = item
            item = item.rstrip()
            if "--viewcomments" in args or "-vc" in args:
              if item.startswith("#"):
                printc(CBEIGE,f"COMMENT: {item}")
            if item.startswith("\endfunc"):
                printc(CGREEN,f"END OF : {function}")
                if func:
                  return printc(CGREEN,"FINISHED RUNNING FUNCTION!")
            if item.startswith("#") == False and item.startswith("\endfunc") == False:
              item = item.replace("*getargs",str(argz).rstrip())
              item = item.replace("*getplatform",str(sys.platform).rstrip())
              item = item.replace("*getvars",str(vars))


              lzma = False
              dp = False
              name = ""

              

              if item.startswith("@dp"):
                dp = True
                item = item.replace("@dp ","")
              
                
                

              for d in vars:
                item = item.replace(d,vars[d])
                iten = iten.replace(d,vars[d])

              if item.startswith("@cp"):
                lzma = True
                src = ""
                dest = ""
                itemz = item.replace("@cp ","")
                itemz = item.split()
                for word in itemz:
                  if word.startswith("src:"):
                    src = word.replace("src:","")
                  if word.startswith("dest:"):
                    dest = word.replace("dest:","")


                shutil.copyfile(src,dest)


              elif item.startswith("@cfg"):
                dp = True
                lzma = True
                item = item.replace("@cfg ","")
                itex = item.split()
                for word in itex:
                  if word.startswith("name:"):
                    name = word.replace("name:","")
                    printc(CGREY,f"Running project {name}")

              elif item.startswith("@var"):
                
                itez = item.replace("@var ","")
                itex = itez.split("=")
                itez = itez.replace(itex[0],"")
                itez = itez.split(" ",1)
                itex[0] = itex[0].replace(" ","")
                vars[f"*{itex[0]}"] = itez[1]
                print(f"Variable {itex[0]} added")

              elif item.startswith("@input"):
                iten = iten.replace("\n","")

                
                iten = iten.replace("@input ","")
                pointer = ""
                tbi = ""
                itex = iten.split(" ",1)
                for word in itex:
                  if word.startswith("point:"):
                    pointer = word.replace("point:","")
                    tbi = iten.replace(f"point:{pointer} query:","")
                query = input(tbi)
                vars[f"*{pointer}"] = query

                
                



              elif item.startswith("@delf"):
                lzma = True
                target = ""
                itemz = item.replace("@delf ","")
                itemz = item.split()
                for word in itemz:
                  if word.startswith("target:"):
                    target = word.replace("target:","")
                os.remove(target)

              elif item.startswith("@deld"):
                lzma = True
                target = ""
                itemz = item.replace("@deld ","")
                itemz = item.split()
                for word in itemz:
                  if word.startswith("target:"):
                    target = word.replace("target:","")
                shutil.rmtree(target)

              elif item.startswith("@create"):
                lzma = True
                target = ""
                itemz = item.replace("@create ","")
                itemz = item.split()
                for word in itemz:
                  if word.startswith("name:"):
                    target = word.replace("name:","")
                os.system(f"touch {target}")
            

              elif item.startswith("@mv"):
                lzma = True
                src = ""
                dest = ""
                itemz = item.replace("@mv ","")
                itemz = item.split()
                for word in itemz:
                  if word.startswith("src:"):
                    src = word.replace("src:","")
                  if word.startswith("dest:"):
                    dest = word.replace("dest:","")

                shutil.move(src,dest)

              elif item.startswith("@rename"):
                lzma = True
                src = ""
                dest = ""
                item = item.replace("@rename ","")
                item = item.split()
                for word in item:
                  if word.startswith("src:"):
                    src = word.replace("src:","")
                  if word.startswith("target:"):
                    dest = word.replace("target:","")

                shutil.move(src, dest)


              elif item.startswith("@reqOS"):
                lzma = True
                item = item.replace("@reqOS ","")
                item = item.split(",")
                if sys.platform not in item:
                    raise RuntimeError(f"OS not supported. RequiredOS: {item} YourOS: {sys.platform}")

              elif item.startswith("@uOS"):
                  lzma = True
                  item = item.replace("@uOS ","")
                  item = item.split(",")
                  if sys.platform in item:
                      raise RuntimeError(f"OS not supported. UnsupportedOS: {item} YourOS: {sys.platform}")

              elif item.startswith("@dl"):
                  lzma = True
                  url = ""
                  output = ""
                  item = item.replace("@dl ","")
                  itemz = item.split()
                  for itex in itemz:
                      if itex.startswith("url:"):
                          url = itex.replace("url:","")
                      if itex.startswith("opt:"):
                          output = itex.replace("opt:","")
                  if "-y" not in args and "-n" not in args:
                      printc(CYELLOW,"Download Query:")
                      query = input(f"""download {url} "y/n" ? """)
                  else:
                      if "-n" in args:
                          query = "n"
                      if "-y" in args:
                          query = "y"
                  if query == "y":
                      download(url,output)
                  if query == "n":
                      printc(CRED,"Aborted download")


              elif item.startswith("@addpkg"):
                  lzma = True
                  pkg = ""
                  lang = ""
                  default = ""
                  flags = ""
                  item = item.replace("@addpkg ","")
                  itemz = item.split()
                  for word in itemz:
                      if word.startswith("pkg:"):
                          pkg = word.replace("pkg:","")
                      if word.startswith("lang:"):
                          lang = word.replace("lang:","")
                      if word.startswith("pm:"):
                          default = word.replace("pm:","")
                      if word.startswith("flags:"):
                          flags = word.replace("flags:","")
                          flags = flags.replace("/"," ")
                  if default != "":
                      printc(CGREEN,f"{default} install {pkg} {flags}")
                      run(f"{default} install {pkg} {flags}")
                  else:
                      if lang in ["py","python"]:
                          printc(CGREEN,f"pip install {pkg} {flags}")
                          run(f"pip install {pkg} {flags}")
                      elif lang in ["js","javascript"]:
                          printc(CGREEN,f"npm install {pkg} {flags}")
                          run(f"npm install {pkg} {flags}")
                      elif lang in ["deb","apt"]:
                          print(f"apt install {pkg} {flags}")
                          run(f"apt install {pkg} {flags}")

              elif item.startswith("@reqSR") and func == False:
                lzma = True
                ok = "ok"




              else:
                  if item.startswith("@reqSR") and func:
                    item = item.replace("@reqSR ","")



                  if item.endswith(":") and item.startswith("@function"):
                    print(CRED,f"Running {item}")
                    function = item
                    line = 0


                  else:
                    if xylo:
                      tex += f"\n{item}"
                    else:
                      line += 1
                      printc(CVIOLET2,f"Running line {line} of {function}")
                      if item.startswith("@python def") == False and dp == False and item.startswith("@function") == False:
                        print(CBLUE2,item)

                      if item.startswith("@q "):
                        run(item.replace("@q ",""))
                      elif item.startswith("@python "):
                        item = item.replace("@python ","")
                        if item.startswith("def") or item.startswith("@exec"):
                          item = item.replace("@exec ","")
                          printc(CRED,"Exectuting python function!")

                          item = item.replace("||","\n")
                          item = item.replace("?|?","  ")
                          printc(CGREEN,item)
                          exec(str(item))

                        else:
                          item = item.replace("||","\n")
                          item = item.replace("?|?","  ")
                          printc(CRED,str(eval(item)))
                      else:
                        os.system(item)
              if lzma and dp == False:
                print(CBLUE2,item)
      elif "Makefile" in files:
        printc(CVIOLET,"Running make ...")
        run("make")
default(x)