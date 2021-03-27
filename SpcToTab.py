#!/usr/bin/env python
import fileinput
import subprocess

def GetFileNames():
	with open("out.txt","w") as out:
		print(subprocess.run(["git","diff","--name-only"], stdout=out))
	with open("out.txt", "r") as out:
		print(out)

def main(filename):
	with open(filename, "r") as file:
		filedata=file.read()
	filedata=filedata.replace("    ","\t")
	with open(filename, "w") as file:
		file.write(filedata)


if __name__ == "__main__":
	GetFileNames()
	main("test.py")
