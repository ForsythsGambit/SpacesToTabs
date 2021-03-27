#!/usr/bin/env python
import fileinput
import subprocess

def GetChangedFiles():
	with open("out.txt","w") as out:
		subprocess.run(["git", "show","-q"], stdout=out)
	

def CleanGitShow():
	with open("out.txt", "r") as out:
		lines=out.readlines()
	with open("out.txt", "w") as out:
		for line in lines:
			if "commit" in line.strip("\n"):
				out.write(line)
				hash=line
				hash=hash.replace("commit ","")
	with open("out.txt","w") as out:
		out.write(hash)

def main(filename):
	with open(filename, "r") as file:
		filedata=file.read()
	filedata=filedata.replace("    ","\t")
	with open(filename, "w") as file:
		file.write(filedata)
if __name__ == "__main__":
	GetChangedFiles()
	CleanGitShow()
	main("test.py")
