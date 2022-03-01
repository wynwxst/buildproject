#!/usr/bin/env python3
import os
#import proj as p
try:
  import time
  import sys
  from flags import Flags
  import subprocess

  import sys
  from sys import platform
  import json
  import base64
  import shutil

  from tqdm import tqdm
  

except ImportError:
  print("Installing dependencies of build...")
  os.system("pip install tqdm")
  os.system("pip install bashflags.py")
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

import json
import os
import sys


pos = ["name","run","version","dependencies","modules","projects","authors"]
class mainz:
  def test(arg):
    
    if arg == "init":
      tw = {}
      os.system(f"mkdir {os.getcwd()}/tests")
      os.system(f"cd {os.getcwd()}/tests && touch tests.json")
      tw["preload"] = "echo what to run before a test eg. pip install etc or compile something"
      tw["run"] = "echo what to run for each test eg. `python` so python <testfile>"
      tw["ignore"] = ["files to ignore eg. `.env`"]
      with open(f"{os.getcwd()}/tests/tests.json","w") as x:
        json.dump(tw,x)
      printc(CGREEN,"Initalized tests!\nConfigure tests/tests.json as needed")
    else:
        
      files = []
      d = {}
      for file in os.listdir(f"{os.getcwd()}/tests/"):
        if file.endswith(".json") == False:
          files.append(file)
      with open(f"{os.getcwd()}/tests/tests.json") as x:
        c = json.load(x)
      tr = c["run"]
      for item in c["ignore"]:
        files.remove(item)
      amt = 1
      for item in files:
        print(f"{amt}. {item}")
        d[amt] = item
        amt += 1
      q = input("> ")
      q = int(q)
      printc(CRED,f"running test no.{q}")
      printc(CWHITE,"............")
      fr = d[q]
      pre = d["preload"]
      os.system(f"cd {os.getcwd()}/tests && {pre}")
      os.system(f"cd {os.getcwd()}/tests && {tr} {fr}")
      
  def openproj():
    try:
      with open(f"{os.getcwd()}/build.proj") as w:
        content = w.read()
        if content == "":
          with open(f"{os.getcwd()}/build.proj","w") as x:
            x.write("{}")
  
      with open(f"{os.getcwd()}/build.proj") as w:
        content = w.read()
  
        
          
        x = json.loads(content)
      return x
    except:
      return None

  def writeproj(proj):
    x = {}

    x = json.dumps(proj,indent=4)


    with open(f"{os.getcwd()}/build.proj","w") as w:
      w.write(x)



  def structproj(): # just a ref
    
    proj = mainz.openproj()

    # main struct

    name = proj["name"]
    author = proj["authors"]
    ver = proj["version"]
    run = proj["run"]
    run = proj["language"]
    deps = proj["dependencies"]
    mods = proj["modules"]



    # projects struct
    x = "example" # insert project name
    path = proj["projects"][x] # path to .project file


    

  def parseproj(opt,arg,args): # just a ref
    
    proj = mainz.openproj()

    # main struct
    try:

      name = proj["name"]
      authors = proj["authors"]
      ver = proj["version"]
      run = proj["run"]
      deps = proj["dependencies"]
      mods = proj["modules"]
      projects = []
      for item in proj["projects"]:
        projects.append(item)
    except:
      if arg != "init":
        return print("ERROR: values not found")



    if opt == "proj":
      if arg == "info":
        print(f"NAME: {name}\nAUTHORS: {authors}\nVERSION: {ver}")
      if arg == "init":
        os.system(f"touch {os.getcwd()}/build.proj")
        proj = mainz.openproj()
        proj["name"] = "Name"
        proj["authors"] = []
        proj["version"] = "0.0.1"
        proj["language"] = "<programming language eg. python, use full forms like javascript NOT js>"
        proj["run"] = "echo You can use Buildfile by replacing this string with 'Buildfile' "
        proj["dependencies"] = ["echo You can use Installfile by replacing this string with 'Installfile'","echo eg. pip install <package>"]
        proj["modules"] = ["https://pathtozipwithlocalmodules.com/module.zip"]
        proj["projects"] = []
        mainz.writeproj(proj)
      if arg == "set" or arg == "add":
        msg = ""
        val = args[0]
        toset = ""
        for item in args:
          if item != args[0]:
            if item == args[len(args)-1]:
              toset += f"{item}"
            else:
              toset += f"{item} "

        posx = pos
        posx.remove("projects")



        if val not in posx:
          return print("Value does not exist in build.proj")
        proj = mainz.openproj()
        if val in ["dependencies","modules","authors","projects"]:
          if toset in proj[val]:
            proj[val].remove(toset)
            msg = "removed"
          else:
            proj[val].append(toset)
            msg = "added"
          
        else:
          proj[val] = toset
          msg = "set"
        mainz.writeproj(proj)
        print(f"Successfully {msg} '{val}' as '{toset}'")
      if arg == "run":
        proj = mainz.openproj()
        run = proj["run"]
        if run == "Installfile":
          default({"x":"t","file":"Installfile","args":args})
        else:
          os.system(run)
      if arg == "dependencies" or arg == "deps":
        proj = mainz.openproj()
        run = proj["dependencies"]
        if deps[0] == "Buildfile":
          default({"x":"t","args":args})
        else:
          for item in deps:
            os.system(item)







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
    print('help : this command\n')
    print('build : build a project\n')
    print('install : install a project\n')
    print('sendargs : send arguments to a project\n')
    print('runfunc : run a specialized function\n')
    print('proj : configure a project\n')

def printc(color,*text):
  CEND      = '\33[0m'
  print(color + text[0] + CEND)



def run(command):
    subprocess.check_output(command,shell=True)

def flags():

    advanced = ["help","sendargs =","runfunc =","build","install","proj ="]


    argv = sys.argv
    bashflags = ""


    try:
      
      bashflags = Flags(argv)


    except:
        printc(CRED,"ERROR: Invalid arguments provided.")
        send_help()

    opt = bashflags.flag
    arg = bashflags.arg
    args = bashflags.args
  
    

    opt = opt.rstrip()
    opt = opt.replace(" ","")
    opt = opt.lower()
    if opt in [""]:
      return {"x":"t","args":args}

    if opt in ["-h","help"]:
      send_help()

    if opt in ["proj"]:
      mainz.parseproj(opt,arg,args)

    if opt in ["test"]:
      mainz.test(arg)
      
    if opt in ["sendargs"]:
      return {"x":"t","args":sys.argv}
    if opt in ["build"]:
      return {"x":"t","args":args}
    if opt in ["install"]:
      return {"x":"t","file":"Installfile","args":args}
    if opt in ["runfunc","-r"]:
      return {"x":"t","args":args,"func":arg}








def default(x):
  if x != None:
    if x["x"] == "t":
      file = f"Buildfile"
      try:
        file = x["file"]
      except KeyError:
        file = f"Buildfile"

      args = x["args"]
      argz = ""

      for item in args:
        if item not in ["build","build.py","main.py","sendargs"]:
          if item != args[len(args)-1]:
            argz += f"{item},"
          else:
            argz += f"{item}"
      files = []
      for filex in os.listdir(os.getcwd()):
        files.append(filex)

      if file in files:
        xylo = False
        tex = ""
        line = 0
        function = ""
        
        printc(CVIOLET,"Running build ...")
        f = open(f"{os.getcwd()}/{file}", "r")
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
            if "viewcomments" in args or "-vc" in args:
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
              from datetime import datetime

              now = datetime.now()

              current_time = now.strftime("%H:%M:%S")
              item = item.replace("*getime",current_time)


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

r = True 

def launch():
  x = flags()
  default(x)


