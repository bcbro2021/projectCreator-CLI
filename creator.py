import sys, os

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


projectName = sys.argv[1]
projectLang = sys.argv[2]
projectType = sys.argv[3]

#const val
python = ["""import src\nsrc.main()""",
          """import sys, os\n\ndef main():\n    print('Hello World')""",
          "from ursina import *\n\nApp = Ursina()\n\nApp.run()"]

def pythonlang():
    #creates the first folder
    try:
        os.mkdir(projectName)
        os.chdir(projectName)
    except FileExistsError:
        print(f"{c.FAIL}Project Already Exists!")
        sys.exit()

    #does the rest
    #creates the (projectName).py file
    with open(f"{projectName}.py", "w") as mainFile:
        mainFile.write(python[0])

    #makes and chdir towards src
    os.mkdir("src")
    os.chdir("src")

    #creates the __init__.py file
    with open("__init__.py", "w") as initFile:
        initFile.write("from .main import *")

    #empty project creation
    if projectType == "empty":
		#creates the main.py fil
        with open("main.py", "w") as File:
            File.write(python[1])
        #close the program
        sys.exit()

    elif projectType == "game":
        #creates the main.py file
        with open("main.py", "w") as File:
            File.write(python[2])
        #close the program
        sys.exit()

def cpplang():
    #creates the first folder
    try:
        os.mkdir(projectName)
    except FileExistsError:
        print(f"{c.FAIL}Project Already Exists!")
        sys.exit()

    #does the rest
    os.chdir(projectName)

    if projectType == "empty":
		#create main.cpp file
        with open(f"main.cpp", "w") as MainFile:
            MainFile.write('#include <iostream>\n\nusing namespace std;\n\nint main(){\n    cout << "Hello World" << endl;\n    return 0;\n}')

        with open("build.sh", "w") as buildFile:
            buildFile.write(f'g++ -o main main.cpp\n./main')
            os.system("chmod u=rwx,g=r,o=r build.sh")

def main():
	if projectLang == "python":
		pythonlang()
	elif projectLang == "c++":
		cpplang()

main()
