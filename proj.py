import json
import os
import __init__ as build

pos = ["name","run","version","dependencies","modules","projects","authors"]
class main:
  def openproj():
    with open(f"{os.getcwd()}/build.proj") as w:
      content = w.read()
      if content == "":
        with open(f"{os.getcwd()}/build.proj","w") as x:
          x.write("{}")

    with open(f"{os.getcwd()}/build.proj") as w:
      content = w.read()

      
        
      x = json.loads(content)
    return x

  def writeproj(proj):
    x = {}

    x = json.dumps(proj,indent=4)


    with open(f"{os.getcwd()}/build.proj","w") as w:
      w.write(x)



  def structproj(): # just a ref
    
    proj = main.openproj()

    # main struct

    name = proj["name"]
    author = proj["authors"]
    ver = proj["version"]
    run = proj["run"]
    deps = proj["dependencies"]
    mods = proj["modules"]



    # projects struct
    x = "example" # insert project name
    path = proj["projects"][x] # path to .project file


    

  def parseproj(opt,arg,args): # just a ref
    
    proj = main.openproj()

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
    except KeyError:
      if arg != "init":
        return print("ERROR: values not found")



    if opt == "--proj":
      if arg == "info":
        print(f"NAME: {name}\nAUTHORS: {authors}\nVERSION: {ver}")
      if arg == "init":
        os.system(f"touch {os.getcwd()}/build.proj")
        proj = main.openproj()
        proj["name"] = "Name"
        proj["authors"] = []
        proj["version"] = "0.0.1"
        proj["run"] = "echo You can use Installfile by replacing this string with 'Installfile' "
        proj["dependencies"] = ["echo You can use Buildfile by replacing this string with 'Buildfile' ","echo eg. pip install <package>"]
        proj["modules"] = ["https://pathtozipwithlocalmodules.com/module.zip"]
        proj["projects"] = []
        print(proj)
        main.writeproj(proj)
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
        proj = main.openproj()
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
        main.writeproj(proj)
        print(f"Successfully {msg} '{val}' as '{toset}'")
      if arg == "run":
        proj = main.openproj()
        run = proj["run"]
        if run == "Installfile":
          build.default({"x":"t","file":"Installfile","args":args})
        else:
          os.system(run)
      if arg == "dependencies" or arg == "deps":
        proj = main.openproj()
        run = proj["dependencies"]
        if deps[0] == "Buildfile":
          build.default({"x":"t","args":args})
        else:
          for item in deps:
            os.system(item)




