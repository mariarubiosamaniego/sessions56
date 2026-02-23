#we will open the file and read it

try:
    fd = open("text.txt")
    print("File opened")
except FileNotFoundError:
    print("Sorry, file not found")

#if something is wrong with how to read, change the interpreter on settings to pythonprojects 3.14,
# because it probably is in pythingmyscprojects 3.14

print(fd.read())
print("File read")
fd.close()  #to show that we are done

#another simpler way
with open("text.txt", "r") as fd:
    print(fd.read())

#smarter way to read: line by line bc fd reads the whole project, if it's too big it crashes
with open("text.txt", "r") as fd:
    for line in fd:
        #print(line) adds 2 enters so we just add that we have to add nothing at the end
        print(line, end="")
        
