file=input("Enter file name: ")
with open(file, "a") as f:
    data=input("Enter text to write in file : ")
    f.write("\n")
    f.write(data)
    f.write("\n")
    data=input("Enter additional text to append in file : ")
    f.write(data)
with open(file, "r") as f:
    while True:
        data = f.readline()
        if data == "":
           break
        else:
           data = data.strip()
           print(f"{data}\n")
