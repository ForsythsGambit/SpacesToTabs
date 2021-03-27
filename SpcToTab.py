#!/usr/bin/env python
import fileinput

def main(filename):
	with open(filename, "r") as file:
		filedata=file.read()
	filedata=filedata.replace("    ","\t")
	with open(filename, "w") as file:
		file.write(filedata)
if __name__ == "__main__":
	main("test.py")
