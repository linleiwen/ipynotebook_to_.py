#https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
import sys,json
import datetime
now = datetime.datetime.now()
f = open(sys.argv[1], 'r') #input.ipynb
j = json.load(f)
of = open(sys.argv[2], 'w') #output.py
of.write("'''__author__:Leiwen Lin''' " + "\n")
of.write("'''__maintainer__:'Leiwen Lin''' " + "\n")
of.write(f"'''__createtime__:{str(now)}''' " + "\n")
if j["nbformat"] >=4:
        for i,cell in enumerate(j["cells"]):
                #of.write("#cell "+str(i)+"\n")
                for line in cell["source"]:
                        of.write(line)
                of.write('\n\n')
else:
        for i,cell in enumerate(j["worksheets"][0]["cells"]):
                #of.write("#cell "+str(i)+"\n")
                for line in cell["input"]:
                        of.write(line)
                of.write('\n\n')

of.close()