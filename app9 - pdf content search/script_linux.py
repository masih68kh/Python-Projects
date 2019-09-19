
import os
import subprocess

while True:
    path = input("Enter the path you want to search in: ")
    if path[-1] == "/":
        break
    else:
        print("Enter '/' at the end of your directory")
        print(repr(path[-1]))

look_for = input("Enter the word(s) you are looking for: ")

subprocess.call("./find.sh"+' '+ path, shell=True)

ls = os.listdir('./txts/')
for file_name in ls:
    with open('./txts/'+file_name, 'r') as fp:
        content = fp.read().splitlines()
        for num, line in enumerate(content):
            if look_for.lower() in line.lower():
                print(file_name[:-4] + '\t@ line ' + str(num+1))

subprocess.call("./remove.sh", shell=True)
