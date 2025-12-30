import os
file=input("Enter file name: ")
i=1
if os.path.exists(file):
    print("Reading file content : ")
try :
    with open(file, "r") as f:
         while True:
            data=f.readline()
            if data=="":
                break
            else :
                data=data.strip()
                print(f"Line{i}: {data}")
                i=i+1
except FileNotFoundError :
         print(f" Error : The File {file} was not found")


