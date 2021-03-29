#!/usr/bin/env python
import fileinput
import subprocess

def GetFileNames():
	files=[]
	with open("out.txt","w") as out:
		#cmd: git diff --name-only
		subprocess.run(["git","diff","--name-only"], stdout=out)
	with open("out.txt", "r") as out:
		lines=out.readlines()
		for line in lines:
			files.append(line)
	return files

def ReplaceSpaces(filename):
	with open(filename, "r") as file:
		filedata=file.read()
	filedata=filedata.replace("    ","\t")
	with open(filename, "w") as file:
		file.write(filedata)


if __name__ == "__main__":
	files=GetFileNames()
	for x in range(0,len(files)):
		files[x]=files[x].rstrip("\n")
	for file in files:
		if file != "SpcToTab.py":
			ReplaceSpaces(file)
		else:
			print("cant operate on self")
