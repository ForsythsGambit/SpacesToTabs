#!/usr/bin/env python
import fileinput
import subprocess

def GetChangedFiles():
	return subprocess.run(["git", "show"])

def main(filename):
	with open(filename, "r") as file:
		filedata=file.read()
	filedata=filedata.replace("    ","\t")
	with open(filename, "w") as file:
		file.write(filedata)
if __name__ == "__main__":
	print(GetChangedFiles())
	main("test.py")
