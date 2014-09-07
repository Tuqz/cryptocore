import importlib

modules = []
functions = []
f = open("files.txt", 'r')
for line in f:
	space = 0
	i = 0
	while i < len(line):
		if(line[i] == ' '):
			space = i
			break
		i += 1
	modules.append(importlib.import_module(line[:space]))
	functions.append(getattr(modules[-1], line[space+1:-1]))
f.close()

f = open("passwords.txt", 'r')
passwords = []
for line in f:
	passwords.append(line)
f.close()

filename = input("Please enter the relative path of the file you wish to decode\n")
f = open(filename, 'r')
lines = []
for line in f:
	lines.append(line[:-1])
f.close()
contents = ""
for line in lines:
	contents += line

for password in passwords:
	for function in functions:
		out = function(contents, password)
		print(out)

