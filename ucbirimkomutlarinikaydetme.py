
import subprocess

command=raw_input("Command? ")
proc=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,)
output=proc.communicate()[0]
fileName=command+".txt"

dsy=open(fileName,"w")
dsy.write(output)
dsy.close()

