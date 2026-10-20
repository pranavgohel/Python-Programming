import os
import sys

print("----------OS Module----------")
print("current working directory:",os.getcwd())
print("list of files and directories in the current working directory is:",os.listdir())
print("Current user:",os.getlogin())
print("Absolute path",os.path.abspath(__file__))
print("Relative path",os.path.relpath(__file__))

print("----------SYS Module----------")
print("Python version is",sys.version)
print("Python version info is",sys.version_info)
print("Python path is",sys.path)
