import os, subprocess

print("Type in file name : ")
file_in = input(str())
file_in = file_in + ".in"
print(file_in)

print("Type in path to file : ")
path = input(str())
print(path)

print("Type in output file _name_ ('name'.dump) : ")
savefname = input(str())
print(savefname)

os.system ("cd" +" "+ path)
if not os.path.isdir("inn"):
     os.mkdir("inn")
else:
    os.system("folder is True")

if not os.path.isdir("Out"):
     os.mkdir("Out")
else:
    os.system("folder is True")

if not os.system("lmp_mpi -in" +" "+ file_in):
    os.system("lmp_serial -in" +" "+ file_in)

os.rename(savefname, "OUT" + savefname)


